# Grado SR60e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.0; 49 -1.6; 54 -2.3; 60 -3.0; 66 -3.6; 72 -4.0; 79 -4.4; 87 -4.7; 96 -5.0; 106 -5.2; 116 -5.4; 128 -5.5; 141 -5.5; 155 -5.4; 170 -5.2; 187 -5.0; 206 -4.8; 227 -4.7; 249 -4.7; 274 -4.7; 302 -4.5; 332 -4.5; 365 -5.2; 402 -5.3; 442 -5.1; 486 -5.0; 535 -4.8; 588 -4.6; 647 -4.4; 712 -4.1; 783 -3.9; 861 -3.6; 947 -3.5; 1042 -3.5; 1146 -3.6; 1261 -3.9; 1387 -4.3; 1526 -5.2; 1678 -6.5; 1846 -10.3; 2031 -12.7; 2234 -12.1; 2457 -10.4; 2703 -8.6; 2973 -7.0; 3270 -6.2; 3597 -8.7; 3957 -10.1; 4353 -6.3; 4788 -4.7; 5267 -6.9; 5793 -7.2; 6373 -8.1; 7010 -10.9; 7711 -12.9; 8482 -13.6; 9330 -12.5; 10263 -10.5; 11289 -8.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 29 Hz   |  0.58 | 6.4 dB   |
| Peaking | 2147 Hz |  2.05 | -11.3 dB |
| Peaking | 3062 Hz |  0.2  | 5.4 dB   |
| Peaking | 3851 Hz |  5.8  | -6.3 dB  |
| Peaking | 8333 Hz |  1.35 | -11.3 dB |
| Peaking | 253 Hz  |  0.99 | 3.3 dB   |
| Peaking | 277 Hz  |  0.6  | -2.4 dB  |
| Peaking | 1598 Hz |  2.22 | 0.9 dB   |
| Peaking | 1907 Hz | 10.6  | -1.7 dB  |
| Peaking | 4675 Hz | 16.22 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20SR60e/Grado%20SR60e.png)