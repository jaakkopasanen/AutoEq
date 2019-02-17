# Beyerdynamic DT 1770 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.2; 25 -4.4; 28 -4.7; 31 -5.0; 34 -5.1; 37 -5.2; 41 -5.3; 45 -5.3; 49 -5.3; 54 -5.3; 60 -5.4; 66 -5.6; 72 -5.8; 79 -6.1; 87 -6.5; 96 -6.9; 106 -7.3; 116 -7.5; 128 -7.4; 141 -7.1; 155 -6.5; 170 -5.5; 187 -4.0; 206 -2.5; 227 -1.4; 249 -1.8; 274 -3.3; 302 -5.0; 332 -6.3; 365 -6.9; 402 -6.9; 442 -6.8; 486 -6.9; 535 -6.9; 588 -6.8; 647 -6.7; 712 -6.5; 783 -6.2; 861 -5.9; 947 -5.6; 1042 -5.4; 1146 -5.2; 1261 -5.2; 1387 -5.3; 1526 -5.5; 1678 -5.6; 1846 -5.1; 2031 -4.4; 2234 -5.2; 2457 -4.3; 2703 -3.5; 2973 -2.6; 3270 -2.2; 3597 -2.3; 3957 -0.5; 4353 -2.3; 4788 -6.8; 5267 -6.8; 5793 -7.4; 6373 -10.0; 7010 -8.2; 7711 -8.7; 8482 -9.6; 9330 -8.0; 10263 -5.5; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1770 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1770 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 15 Hz    |  0.15 | 1.2 dB  |
| Peaking | 210 Hz   |  0.53 | -5.2 dB |
| Peaking | 228 Hz   |  1.76 | 9.3 dB  |
| Peaking | 3842 Hz  |  1.64 | 6.2 dB  |
| Peaking | 6332 Hz  |  1.14 | -5.1 dB |
| Peaking | 1113 Hz  |  3.91 | 0.6 dB  |
| Peaking | 4770 Hz  | 12.24 | -2.6 dB |
| Peaking | 8665 Hz  |  0.75 | 1.0 dB  |
| Peaking | 8750 Hz  |  4.03 | -3.2 dB |
| Peaking | 10226 Hz |  3.27 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%201770%20PRO/Beyerdynamic%20DT%201770%20PRO.png)