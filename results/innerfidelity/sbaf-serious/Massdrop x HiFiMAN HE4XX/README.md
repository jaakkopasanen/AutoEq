# Massdrop x HiFiMAN HE4XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 0.0; 23 3.2; 25 2.8; 28 2.4; 31 2.1; 34 1.9; 37 1.8; 41 1.7; 45 1.6; 49 1.5; 54 1.3; 60 0.7; 66 0.4; 72 0.2; 79 -0.0; 87 -0.3; 96 -0.6; 106 -0.8; 116 -0.9; 128 -1.2; 141 -1.3; 155 -1.6; 170 -1.6; 187 -1.8; 206 -1.9; 227 -1.7; 249 -1.5; 274 -1.4; 302 -1.6; 332 -1.9; 365 -2.2; 402 -1.9; 442 -1.3; 486 -0.7; 535 -1.3; 588 -1.1; 647 -1.2; 712 -1.4; 783 -0.2; 861 -0.4; 947 -0.3; 1042 0.2; 1146 0.6; 1261 1.1; 1387 0.9; 1526 1.1; 1678 1.6; 1846 1.9; 2031 1.6; 2234 1.1; 2457 -0.1; 2703 -0.9; 2973 -1.2; 3270 -0.7; 3597 -0.1; 3957 -0.2; 4353 -3.1; 4788 -2.3; 5267 0.9; 5793 1.0; 6373 -3.1; 7010 -6.0; 7711 -5.4; 8482 -6.2; 9330 -6.1; 10263 -0.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x HiFiMAN HE4XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x HiFiMAN HE4XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.25 | 3.7 dB  |
| Peaking | 242 Hz   | 0.35 | -1.9 dB |
| Peaking | 1969 Hz  | 1.1  | 3.0 dB  |
| Peaking | 2774 Hz  | 1.63 | -2.5 dB |
| Peaking | 8090 Hz  | 2.42 | -6.9 dB |
| Peaking | 3882 Hz  | 4.43 | 2.1 dB  |
| Peaking | 4487 Hz  | 4.05 | -4.3 dB |
| Peaking | 5532 Hz  | 3.96 | 3.9 dB  |
| Peaking | 6753 Hz  | 7.43 | -3.1 dB |
| Peaking | 10935 Hz | 6.06 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20HiFiMAN%20HE4XX/Massdrop%20x%20HiFiMAN%20HE4XX.png)