# Beats EP On-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.3; 25 -4.5; 28 -4.6; 31 -4.7; 34 -4.8; 37 -4.9; 41 -4.9; 45 -4.9; 49 -5.0; 54 -5.2; 60 -5.5; 66 -5.9; 72 -6.2; 79 -6.4; 87 -6.7; 96 -7.0; 106 -7.3; 116 -7.6; 128 -7.9; 141 -8.0; 155 -8.2; 170 -8.2; 187 -8.1; 206 -8.0; 227 -7.8; 249 -7.3; 274 -6.8; 302 -6.1; 332 -5.8; 365 -5.5; 402 -5.4; 442 -5.2; 486 -4.9; 535 -4.5; 588 -4.1; 647 -3.8; 712 -3.4; 783 -3.2; 861 -3.1; 947 -3.2; 1042 -3.4; 1146 -3.6; 1261 -3.9; 1387 -4.2; 1526 -4.7; 1678 -5.0; 1846 -5.4; 2031 -5.8; 2234 -5.3; 2457 -4.2; 2703 -3.1; 2973 -3.1; 3270 -3.1; 3597 -2.7; 3957 -2.2; 4353 -3.5; 4788 -6.3; 5267 -3.9; 5793 -0.5; 6373 -0.8; 7010 -4.4; 7711 -6.4; 8482 -6.3; 9330 -5.2; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats EP On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats EP On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 164 Hz  | 0.85 | -3.4 dB |
| Peaking | 820 Hz  | 1.36 | 2.2 dB  |
| Peaking | 3511 Hz | 2.85 | 2.5 dB  |
| Peaking | 6125 Hz | 5.43 | 5.7 dB  |
| Peaking | 7879 Hz | 3.23 | -2.1 dB |
| Peaking | 22 Hz   | 0.94 | 0.8 dB  |
| Peaking | 2045 Hz | 4.03 | -1.4 dB |
| Peaking | 2688 Hz | 7.21 | 1.3 dB  |
| Peaking | 4796 Hz | 2.91 | 2.3 dB  |
| Peaking | 4804 Hz | 6.89 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20EP%20On-Ear/Beats%20EP%20On-Ear.png)