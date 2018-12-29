# Read Heath Acoustics MA750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 -5.9; 23 -5.9; 25 -5.9; 28 -5.9; 31 -5.9; 34 -6.0; 37 -6.0; 41 -5.9; 45 -5.9; 49 -5.9; 54 -5.9; 60 -6.0; 66 -6.1; 72 -6.1; 79 -6.3; 87 -6.4; 96 -6.6; 106 -6.6; 116 -6.5; 128 -6.6; 141 -6.6; 155 -6.6; 170 -6.5; 187 -6.3; 206 -6.2; 227 -5.9; 249 -5.7; 274 -5.4; 302 -5.1; 332 -4.7; 365 -4.3; 402 -3.8; 442 -3.2; 486 -3.0; 535 -2.5; 588 -1.6; 647 -1.2; 712 -0.8; 783 -0.3; 861 -0.2; 947 -0.0; 1042 -0.0; 1146 0.2; 1261 0.3; 1387 0.3; 1526 -0.1; 1678 -0.1; 1846 0.3; 2031 0.7; 2234 1.0; 2457 1.4; 2703 1.2; 2973 0.8; 3270 -0.2; 3597 -1.5; 3957 -3.2; 4353 -6.5; 4788 -7.9; 5267 -4.3; 5793 1.1; 6373 4.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.0; 11289 -0.1; 12418 0.0; 13660 -0.9; 15026 -4.6; 16529 -0.7; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Read Heath Acoustics MA750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read Heath Acoustics MA750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.18 | -5.9 dB |
| Peaking | 227 Hz   | 0.69 | -3.5 dB |
| Peaking | 4724 Hz  | 4.18 | -9.4 dB |
| Peaking | 6429 Hz  | 4.71 | 6.1 dB  |
| Peaking | 15131 Hz | 4.68 | -5.1 dB |
| Peaking | 498 Hz   | 1.44 | -1.3 dB |
| Peaking | 671 Hz   | 0.7  | 1.1 dB  |
| Peaking | 2605 Hz  | 2.62 | 1.7 dB  |
| Peaking | 4112 Hz  | 6.65 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20Heath%20Acoustics%20MA750/Read%20Heath%20Acoustics%20MA750.png)