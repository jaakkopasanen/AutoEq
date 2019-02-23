# Skullcandy Navigator
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.0; 25 -10.0; 28 -10.1; 31 -10.1; 34 -10.1; 37 -10.1; 41 -10.1; 45 -10.1; 49 -10.1; 54 -10.2; 60 -10.3; 66 -10.4; 72 -10.6; 79 -10.8; 87 -11.1; 96 -11.3; 106 -11.5; 116 -11.6; 128 -11.9; 141 -12.0; 155 -11.9; 170 -11.8; 187 -11.5; 206 -11.9; 227 -11.9; 249 -11.8; 274 -11.3; 302 -10.9; 332 -10.6; 365 -10.1; 402 -9.6; 442 -8.8; 486 -8.3; 535 -7.7; 588 -6.9; 647 -6.6; 712 -6.4; 783 -6.0; 861 -6.7; 947 -7.2; 1042 -7.4; 1146 -7.4; 1261 -7.7; 1387 -7.6; 1526 -7.8; 1678 -7.2; 1846 -6.7; 2031 -5.9; 2234 -5.1; 2457 -4.2; 2703 -3.6; 2973 -3.3; 3270 -2.6; 3597 -2.4; 3957 -0.5; 4353 -1.2; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Navigator GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Navigator ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.22 | -3.3 dB |
| Peaking | 137 Hz  | 0.8  | -3.6 dB |
| Peaking | 279 Hz  | 1.26 | -3.3 dB |
| Peaking | 1456 Hz | 2.5  | -1.9 dB |
| Peaking | 4555 Hz | 1.13 | 6.3 dB  |
| Peaking | 728 Hz  | 4.7  | 1.1 dB  |
| Peaking | 2613 Hz | 5.36 | 0.9 dB  |
| Peaking | 4589 Hz | 8.85 | -1.5 dB |
| Peaking | 6356 Hz | 2.73 | 4.7 dB  |
| Peaking | 7368 Hz | 1.65 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Navigator/Skullcandy%20Navigator.png)