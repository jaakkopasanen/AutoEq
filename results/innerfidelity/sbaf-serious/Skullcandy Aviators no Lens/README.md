# Skullcandy Aviators no Lens
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.9; 41 -3.1; 45 -4.1; 49 -5.0; 54 -6.0; 60 -6.8; 66 -7.5; 72 -8.1; 79 -8.7; 87 -9.1; 96 -9.5; 106 -9.8; 116 -9.8; 128 -10.0; 141 -10.1; 155 -10.1; 170 -10.0; 187 -9.9; 206 -9.9; 227 -9.7; 249 -9.5; 274 -9.1; 302 -8.8; 332 -8.7; 365 -8.4; 402 -8.2; 442 -8.0; 486 -7.8; 535 -7.6; 588 -7.1; 647 -6.8; 712 -6.6; 783 -6.0; 861 -5.8; 947 -5.4; 1042 -5.0; 1146 -4.3; 1261 -3.6; 1387 -3.9; 1526 -3.4; 1678 -2.4; 1846 -1.5; 2031 -1.3; 2234 -2.0; 2457 -3.1; 2703 -4.8; 2973 -6.4; 3270 -7.1; 3597 -6.2; 3957 -6.7; 4353 -10.5; 4788 -9.9; 5267 -5.7; 5793 -2.4; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.7; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Aviators no Lens GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Aviators no Lens ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.66 | 8.2 dB  |
| Peaking | 104 Hz  | 0.35 | -4.7 dB |
| Peaking | 1840 Hz | 1.37 | 5.2 dB  |
| Peaking | 4518 Hz | 4.23 | -5.6 dB |
| Peaking | 6155 Hz | 4.48 | 6.4 dB  |
| Peaking | 1270 Hz | 2.22 | 1.2 dB  |
| Peaking | 1505 Hz | 3.3  | -1.8 dB |
| Peaking | 2907 Hz | 1.32 | 1.6 dB  |
| Peaking | 3076 Hz | 4.02 | -3.4 dB |
| Peaking | 9393 Hz | 3.86 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Aviators%20no%20Lens/Skullcandy%20Aviators%20no%20Lens.png)