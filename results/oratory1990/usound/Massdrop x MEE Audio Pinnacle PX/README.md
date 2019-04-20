# Massdrop x MEE Audio Pinnacle PX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.8; 25 -2.1; 28 -2.5; 31 -2.8; 34 -3.1; 37 -3.3; 41 -3.6; 45 -3.8; 49 -4.1; 54 -4.4; 60 -4.8; 66 -5.1; 72 -5.4; 79 -5.8; 87 -6.2; 96 -6.5; 106 -6.8; 116 -7.0; 128 -7.2; 141 -7.2; 155 -7.3; 170 -8.4; 187 -8.6; 206 -8.3; 227 -8.0; 249 -7.7; 274 -7.3; 302 -6.8; 332 -6.4; 365 -6.3; 402 -5.9; 442 -5.5; 486 -4.9; 535 -4.3; 588 -3.7; 647 -3.2; 712 -2.6; 783 -1.9; 861 -1.5; 947 -1.3; 1042 -1.3; 1146 -1.5; 1261 -1.8; 1387 -1.7; 1526 -1.2; 1678 -0.5; 1846 -0.5; 2031 -0.8; 2234 -1.6; 2457 -3.0; 2703 -4.6; 2973 -5.3; 3270 -4.8; 3597 -4.0; 3957 -4.0; 4353 -5.1; 4788 -6.6; 5267 -6.9; 5793 -3.6; 6373 -1.1; 7010 -2.0; 7711 -5.3; 8482 -6.0; 9330 -4.4; 10263 -4.4; 11289 -4.6; 12418 -8.1; 13660 -10.7; 15026 -13.0; 16529 -11.3; 18182 -5.5; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x MEE Audio Pinnacle PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x MEE Audio Pinnacle PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.65 | 3.2 dB  |
| Peaking | 192 Hz   | 0.61 | -3.9 dB |
| Peaking | 918 Hz   | 1.19 | 3.5 dB  |
| Peaking | 1830 Hz  | 2.74 | 3.7 dB  |
| Peaking | 15313 Hz | 1.69 | -9.6 dB |
| Peaking | 2934 Hz  | 1.69 | 1.9 dB  |
| Peaking | 2943 Hz  | 3.69 | -3.5 dB |
| Peaking | 4842 Hz  | 5.46 | -2.2 dB |
| Peaking | 5222 Hz  | 7.74 | -2.2 dB |
| Peaking | 6502 Hz  | 5.64 | 4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -9.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Massdrop%20x%20MEE%20Audio%20Pinnacle%20PX/Massdrop%20x%20MEE%20Audio%20Pinnacle%20PX.png)