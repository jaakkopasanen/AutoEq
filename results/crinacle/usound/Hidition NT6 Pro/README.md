# Hidition NT6 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.0; 25 -6.1; 28 -6.4; 31 -6.5; 34 -6.5; 37 -6.6; 41 -6.6; 45 -6.6; 49 -6.7; 54 -6.8; 60 -6.9; 66 -7.0; 72 -7.2; 79 -7.5; 87 -7.7; 96 -7.9; 106 -8.3; 116 -8.5; 128 -8.7; 141 -8.9; 155 -8.9; 170 -9.0; 187 -9.1; 206 -9.1; 227 -9.0; 249 -8.8; 274 -8.6; 302 -8.4; 332 -8.1; 365 -7.8; 402 -7.4; 442 -6.9; 486 -6.4; 535 -5.8; 588 -5.2; 647 -4.5; 712 -3.9; 783 -3.5; 861 -3.5; 947 -3.9; 1042 -4.8; 1146 -6.2; 1261 -7.5; 1387 -8.2; 1526 -8.1; 1678 -7.5; 1846 -6.8; 2031 -6.4; 2234 -6.6; 2457 -6.5; 2703 -5.6; 2973 -4.6; 3270 -4.0; 3597 -3.2; 3957 -0.6; 4353 -0.5; 4788 -0.8; 5267 -5.7; 5793 -6.5; 6373 -4.4; 7010 -5.0; 7711 -9.6; 8482 -13.4; 9330 -11.5; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hidition NT6 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hidition NT6 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 205 Hz   |  0.59 | -2.8 dB |
| Peaking | 855 Hz   |  1.16 | 4.3 dB  |
| Peaking | 1372 Hz  |  1.83 | -3.5 dB |
| Peaking | 4229 Hz  |  2.47 | 6.6 dB  |
| Peaking | 8661 Hz  |  4.65 | -8.1 dB |
| Peaking | 13 Hz    |  0.85 | 1.3 dB  |
| Peaking | 5514 Hz  | 10.78 | -2.9 dB |
| Peaking | 6670 Hz  |  7.56 | 2.7 dB  |
| Peaking | 21057 Hz |  1.7  | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hidition%20NT6%20Pro/Hidition%20NT6%20Pro.png)