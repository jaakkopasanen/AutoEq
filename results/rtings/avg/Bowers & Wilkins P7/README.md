# Bowers & Wilkins P7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.7; 25 -8.9; 28 -9.2; 31 -9.4; 34 -9.4; 37 -9.3; 41 -9.2; 45 -9.0; 49 -8.9; 54 -8.7; 60 -8.7; 66 -8.8; 72 -8.7; 79 -8.5; 87 -8.6; 96 -8.9; 106 -9.3; 116 -9.5; 128 -9.5; 141 -9.4; 155 -9.1; 170 -8.7; 187 -8.1; 206 -7.4; 227 -6.5; 249 -5.7; 274 -4.9; 302 -4.5; 332 -4.3; 365 -4.6; 402 -5.4; 442 -5.7; 486 -5.7; 535 -5.7; 588 -5.8; 647 -5.8; 712 -5.9; 783 -6.0; 861 -6.1; 947 -6.2; 1042 -6.0; 1146 -5.7; 1261 -6.4; 1387 -7.0; 1526 -7.8; 1678 -8.7; 1846 -9.3; 2031 -8.9; 2234 -5.9; 2457 -2.8; 2703 -2.3; 2973 -2.4; 3270 -3.4; 3597 -5.3; 3957 -6.0; 4353 -4.6; 4788 -2.9; 5267 -2.2; 5793 -2.1; 6373 -0.5; 7010 -3.2; 7711 -5.4; 8482 -7.9; 9330 -6.3; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -6.0; 16529 -8.1; 18182 -6.0; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.54 | -3.6 dB |
| Peaking | 131 Hz   | 1.76 | -3.3 dB |
| Peaking | 1918 Hz  | 2.36 | -5.3 dB |
| Peaking | 2618 Hz  | 2.58 | 5.3 dB  |
| Peaking | 6000 Hz  | 3.2  | 4.8 dB  |
| Peaking | 317 Hz   | 3.28 | 2.1 dB  |
| Peaking | 3964 Hz  | 4.86 | -3.2 dB |
| Peaking | 4257 Hz  | 2.09 | 1.9 dB  |
| Peaking | 8606 Hz  | 6.83 | -3.2 dB |
| Peaking | 16690 Hz | 3.08 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20P7/Bowers%20&%20Wilkins%20P7.png)