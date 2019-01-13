# Massdrop x AKG K7XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 0.0; 23 0.2; 25 -0.2; 28 -0.8; 31 -1.2; 34 -1.6; 37 -1.8; 41 -2.1; 45 -2.4; 49 -2.6; 54 -2.9; 60 -3.2; 66 -3.5; 72 -3.7; 79 -4.0; 87 -4.4; 96 -4.7; 106 -4.9; 116 -5.1; 128 -5.2; 141 -5.3; 155 -5.4; 170 -5.4; 187 -5.0; 206 -5.0; 227 -5.1; 249 -5.0; 274 -5.0; 302 -4.9; 332 -4.6; 365 -4.3; 402 -4.0; 442 -3.4; 486 -3.1; 535 -2.6; 588 -1.7; 647 -1.2; 712 -0.5; 783 0.2; 861 0.6; 947 0.2; 1042 0.0; 1146 -0.6; 1261 -1.1; 1387 -2.1; 1526 -3.6; 1678 -5.0; 1846 -5.5; 2031 -5.6; 2234 -4.4; 2457 -1.4; 2703 1.4; 2973 3.5; 3270 3.5; 3597 1.8; 3957 -0.0; 4353 -1.3; 4788 -0.7; 5267 1.4; 5793 1.5; 6373 0.1; 7010 -2.6; 7711 -3.1; 8482 -4.6; 9330 -3.5; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.6; 18182 -3.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x AKG K7XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x AKG K7XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 124 Hz   | 0.52 | -5.0 dB |
| Peaking | 329 Hz   | 1.34 | -2.8 dB |
| Peaking | 1941 Hz  | 2.38 | -6.6 dB |
| Peaking | 3035 Hz  | 3.46 | 5.3 dB  |
| Peaking | 8465 Hz  | 3.89 | -5.0 dB |
| Peaking | 17 Hz    | 1.97 | 1.3 dB  |
| Peaking | 876 Hz   | 3.58 | 1.7 dB  |
| Peaking | 4517 Hz  | 5.45 | -1.9 dB |
| Peaking | 5551 Hz  | 6.29 | 2.7 dB  |
| Peaking | 18250 Hz | 3.11 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20AKG%20K7XX/Massdrop%20x%20AKG%20K7XX.png)