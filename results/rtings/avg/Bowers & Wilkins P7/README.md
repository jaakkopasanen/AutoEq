# Bowers & Wilkins P7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.7; 25 -8.9; 28 -9.2; 31 -9.4; 34 -9.4; 37 -9.4; 41 -9.2; 45 -9.1; 49 -8.9; 54 -8.8; 60 -8.9; 66 -8.9; 72 -8.7; 79 -8.5; 87 -8.6; 96 -8.9; 106 -9.3; 116 -9.5; 128 -9.5; 141 -9.4; 155 -9.2; 170 -8.8; 187 -8.2; 206 -7.5; 227 -6.6; 249 -5.8; 274 -5.1; 302 -4.6; 332 -4.5; 365 -4.8; 402 -5.6; 442 -5.9; 486 -6.0; 535 -6.0; 588 -6.1; 647 -6.2; 712 -6.3; 783 -6.4; 861 -6.4; 947 -6.6; 1042 -6.3; 1146 -6.1; 1261 -6.8; 1387 -7.4; 1526 -8.3; 1678 -9.1; 1846 -9.9; 2031 -9.6; 2234 -6.9; 2457 -4.0; 2703 -3.0; 2973 -2.7; 3270 -3.4; 3597 -5.3; 3957 -6.1; 4353 -4.5; 4788 -3.6; 5267 -2.8; 5793 -2.3; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -7.8; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.1; 16529 -8.3; 18182 -6.2; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.55 | -3.4 dB |
| Peaking | 131 Hz  | 1.81 | -3.2 dB |
| Peaking | 1921 Hz | 2.22 | -5.5 dB |
| Peaking | 2697 Hz | 2.33 | 4.9 dB  |
| Peaking | 6144 Hz | 3.78 | 5.3 dB  |
| Peaking | 318 Hz  | 3.31 | 2.1 dB  |
| Peaking | 3924 Hz | 5.93 | -2.6 dB |
| Peaking | 4331 Hz | 2.44 | 1.6 dB  |
| Peaking | 7408 Hz | 3.7  | 0.2 dB  |
| Peaking | 8454 Hz | 5.86 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20P7/Bowers%20&%20Wilkins%20P7.png)