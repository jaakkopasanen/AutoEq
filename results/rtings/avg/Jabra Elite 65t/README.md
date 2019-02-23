# Jabra Elite 65t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.3; 41 -1.9; 45 -2.3; 49 -2.6; 54 -2.9; 60 -3.5; 66 -4.0; 72 -4.5; 79 -5.0; 87 -5.5; 96 -6.0; 106 -6.6; 116 -7.2; 128 -7.7; 141 -8.2; 155 -8.5; 170 -8.6; 187 -8.7; 206 -8.9; 227 -8.8; 249 -8.6; 274 -8.2; 302 -7.9; 332 -7.7; 365 -7.4; 402 -7.0; 442 -6.5; 486 -6.1; 535 -5.6; 588 -4.9; 647 -4.2; 712 -3.5; 783 -3.3; 861 -3.4; 947 -3.8; 1042 -4.6; 1146 -5.4; 1261 -6.0; 1387 -6.4; 1526 -6.6; 1678 -6.9; 1846 -7.3; 2031 -7.5; 2234 -7.0; 2457 -6.1; 2703 -5.4; 2973 -5.0; 3270 -4.9; 3597 -5.2; 3957 -5.8; 4353 -6.8; 4788 -7.3; 5267 -7.0; 5793 -5.3; 6373 -3.9; 7010 -4.0; 7711 -6.2; 8482 -8.9; 9330 -12.7; 10263 -15.5; 11289 -14.9; 12418 -10.8; 13660 -6.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.41 | 6.2 dB   |
| Peaking | 183 Hz   | 0.73 | -3.1 dB  |
| Peaking | 772 Hz   | 1.75 | 3.8 dB   |
| Peaking | 6773 Hz  | 3.52 | 4.4 dB   |
| Peaking | 10535 Hz | 2.41 | -10.3 dB |
| Peaking | 990 Hz   | 6.22 | 0.6 dB   |
| Peaking | 2042 Hz  | 1.79 | -2.0 dB  |
| Peaking | 3090 Hz  | 1.42 | 2.3 dB   |
| Peaking | 4749 Hz  | 3.53 | -1.7 dB  |
| Peaking | 14233 Hz | 4.49 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2065t/Jabra%20Elite%2065t.png)