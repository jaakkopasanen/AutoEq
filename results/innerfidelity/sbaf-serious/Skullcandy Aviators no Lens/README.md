# Skullcandy Aviators no Lens
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.2; 34 -2.3; 37 -3.3; 41 -4.5; 45 -5.5; 49 -6.4; 54 -7.3; 60 -8.2; 66 -8.9; 72 -9.5; 79 -10.1; 87 -10.5; 96 -10.9; 106 -11.1; 116 -11.2; 128 -11.4; 141 -11.5; 155 -11.5; 170 -11.4; 187 -11.3; 206 -11.3; 227 -11.0; 249 -10.8; 274 -10.5; 302 -10.2; 332 -10.0; 365 -9.8; 402 -9.6; 442 -9.3; 486 -9.2; 535 -9.0; 588 -8.5; 647 -8.2; 712 -7.9; 783 -7.4; 861 -7.2; 947 -6.8; 1042 -6.4; 1146 -5.7; 1261 -5.0; 1387 -5.2; 1526 -4.7; 1678 -3.7; 1846 -2.8; 2031 -2.6; 2234 -3.4; 2457 -4.5; 2703 -6.2; 2973 -7.8; 3270 -8.4; 3597 -7.6; 3957 -8.0; 4353 -11.8; 4788 -11.2; 5267 -7.1; 5793 -3.8; 6373 -2.4; 7010 -4.1; 7711 -6.2; 8482 -7.3; 9330 -9.1; 10263 -8.5; 11289 -7.3; 12418 -6.5; 13660 -6.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Aviators no Lens GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Aviators no Lens ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.72 | 9.1 dB  |
| Peaking | 109 Hz  | 0.25 | -5.8 dB |
| Peaking | 2014 Hz | 1.27 | 5.3 dB  |
| Peaking | 5346 Hz | 0.93 | -9.9 dB |
| Peaking | 6172 Hz | 2.28 | 13.3 dB |
| Peaking | 3134 Hz | 4.71 | -1.6 dB |
| Peaking | 3823 Hz | 4.45 | 3.3 dB  |
| Peaking | 4407 Hz | 6    | -3.3 dB |
| Peaking | 9673 Hz | 3.01 | -3.0 dB |
| Peaking | 9995 Hz | 0.92 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Aviators%20no%20Lens/Skullcandy%20Aviators%20no%20Lens.png)