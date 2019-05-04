# Logitech G533
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.0; 25 -6.2; 28 -6.5; 31 -6.7; 34 -6.7; 37 -6.7; 41 -6.6; 45 -6.4; 49 -6.3; 54 -6.3; 60 -6.3; 66 -6.3; 72 -6.3; 79 -6.3; 87 -6.5; 96 -6.8; 106 -7.0; 116 -7.0; 128 -7.0; 141 -7.0; 155 -7.0; 170 -7.0; 187 -6.8; 206 -6.6; 227 -6.4; 249 -6.4; 274 -6.8; 302 -7.1; 332 -7.2; 365 -6.7; 402 -5.9; 442 -5.3; 486 -5.0; 535 -4.3; 588 -3.7; 647 -3.4; 712 -2.9; 783 -1.9; 861 -1.5; 947 -2.3; 1042 -2.9; 1146 -3.1; 1261 -2.7; 1387 -1.5; 1526 -0.5; 1678 -1.1; 1846 -2.3; 2031 -3.1; 2234 -3.3; 2457 -3.1; 2703 -5.5; 2973 -4.8; 3270 -4.0; 3597 -5.1; 3957 -6.0; 4353 -6.6; 4788 -5.4; 5267 -3.6; 5793 -3.7; 6373 -4.6; 7010 -5.6; 7711 -6.7; 8482 -8.8; 9330 -7.0; 10263 -4.9; 11289 -4.9; 12418 -7.7; 13660 -9.2; 15026 -7.6; 16529 -7.9; 18182 -12.3; 20000 -18.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G533 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G533 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 191 Hz   | 0.13 | -2.1 dB  |
| Peaking | 786 Hz   | 1.4  | 4.2 dB   |
| Peaking | 1601 Hz  | 2.12 | 4.4 dB   |
| Peaking | 12642 Hz | 0.66 | -1.4 dB  |
| Peaking | 19745 Hz | 0.87 | -12.7 dB |
| Peaking | 4435 Hz  | 3.97 | -3.0 dB  |
| Peaking | 5312 Hz  | 2.18 | 2.7 dB   |
| Peaking | 8573 Hz  | 4    | -3.7 dB  |
| Peaking | 10414 Hz | 3.95 | 2.7 dB   |
| Peaking | 16149 Hz | 6.53 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G533/Logitech%20G533.png)