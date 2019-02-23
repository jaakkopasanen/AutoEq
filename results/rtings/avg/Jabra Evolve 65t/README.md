# Jabra Evolve 65t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.7; 31 -2.6; 34 -3.2; 37 -3.7; 41 -4.1; 45 -4.5; 49 -4.7; 54 -5.0; 60 -5.5; 66 -5.8; 72 -6.1; 79 -6.5; 87 -7.0; 96 -7.4; 106 -7.9; 116 -8.4; 128 -8.8; 141 -9.2; 155 -9.5; 170 -9.6; 187 -9.7; 206 -9.7; 227 -9.6; 249 -9.4; 274 -9.1; 302 -8.6; 332 -8.2; 365 -7.9; 402 -7.6; 442 -7.1; 486 -6.5; 535 -5.9; 588 -5.2; 647 -4.5; 712 -4.0; 783 -3.6; 861 -3.1; 947 -3.3; 1042 -4.1; 1146 -5.1; 1261 -5.8; 1387 -6.3; 1526 -6.3; 1678 -6.5; 1846 -6.6; 2031 -6.5; 2234 -5.6; 2457 -4.5; 2703 -3.8; 2973 -3.5; 3270 -3.7; 3597 -4.1; 3957 -5.0; 4353 -6.2; 4788 -6.4; 5267 -6.2; 5793 -4.7; 6373 -3.5; 7010 -4.0; 7711 -6.3; 8482 -9.7; 9330 -11.8; 10263 -13.7; 11289 -14.4; 12418 -12.1; 13660 -8.7; 15026 -8.3; 16529 -11.6; 18182 -11.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Evolve 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Evolve 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.62 | 6.5 dB   |
| Peaking | 204 Hz   | 0.73 | -4.7 dB  |
| Peaking | 4297 Hz  | 0.04 | 2.0 dB   |
| Peaking | 10863 Hz | 1.92 | -10.2 dB |
| Peaking | 17456 Hz | 1.44 | -7.8 dB  |
| Peaking | 878 Hz   | 1.41 | 4.4 dB   |
| Peaking | 1640 Hz  | 0.48 | -3.7 dB  |
| Peaking | 3006 Hz  | 1.48 | 4.4 dB   |
| Peaking | 5838 Hz  | 1.01 | -3.0 dB  |
| Peaking | 6609 Hz  | 2.95 | 6.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Evolve%2065t/Jabra%20Evolve%2065t.png)