# Jabra Evolve 65t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.7; 25 -2.8; 28 -4.0; 31 -4.9; 34 -5.5; 37 -6.0; 41 -6.5; 45 -6.8; 49 -7.0; 54 -7.3; 60 -7.8; 66 -8.2; 72 -8.5; 79 -8.9; 87 -9.3; 96 -9.7; 106 -10.2; 116 -10.7; 128 -11.2; 141 -11.6; 155 -11.9; 170 -12.0; 187 -12.0; 206 -12.0; 227 -12.0; 249 -11.7; 274 -11.4; 302 -11.0; 332 -10.5; 365 -10.2; 402 -9.9; 442 -9.4; 486 -8.8; 535 -8.2; 588 -7.5; 647 -6.9; 712 -6.3; 783 -5.9; 861 -5.5; 947 -5.6; 1042 -6.4; 1146 -7.5; 1261 -8.2; 1387 -8.6; 1526 -8.6; 1678 -8.8; 1846 -8.9; 2031 -8.8; 2234 -7.9; 2457 -6.8; 2703 -6.2; 2973 -5.9; 3270 -6.0; 3597 -6.5; 3957 -7.3; 4353 -8.5; 4788 -8.7; 5267 -8.6; 5793 -7.0; 6373 -5.8; 7010 -5.0; 7711 -8.1; 8482 -12.0; 9330 -14.2; 10263 -16.0; 11289 -16.7; 12418 -14.4; 13660 -11.0; 15026 -10.6; 16529 -13.9; 18182 -13.7; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Evolve 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Evolve 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.93 | 6.0 dB   |
| Peaking | 185 Hz   | 0.56 | -6.3 dB  |
| Peaking | 1743 Hz  | 2.29 | -3.0 dB  |
| Peaking | 10871 Hz | 1.8  | -10.9 dB |
| Peaking | 17406 Hz | 1.41 | -8.8 dB  |
| Peaking | 839 Hz   | 3.72 | 1.9 dB   |
| Peaking | 3180 Hz  | 3.12 | 1.4 dB   |
| Peaking | 4877 Hz  | 1.94 | -2.8 dB  |
| Peaking | 6917 Hz  | 2.64 | 4.5 dB   |
| Peaking | 8528 Hz  | 4.01 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB  |
| Peaking | 16000 Hz | 1.41 | -10.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Evolve%2065t/Jabra%20Evolve%2065t.png)