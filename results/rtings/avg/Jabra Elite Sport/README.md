# Jabra Elite Sport
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.7; 25 -12.7; 28 -12.8; 31 -12.8; 34 -12.8; 37 -12.9; 41 -12.9; 45 -13.0; 49 -13.0; 54 -13.1; 60 -13.2; 66 -13.3; 72 -13.4; 79 -13.5; 87 -13.6; 96 -13.7; 106 -13.7; 116 -13.7; 128 -13.6; 141 -13.4; 155 -13.1; 170 -12.7; 187 -12.2; 206 -11.7; 227 -11.1; 249 -10.3; 274 -9.4; 302 -8.2; 332 -7.3; 365 -6.7; 402 -6.3; 442 -6.2; 486 -6.0; 535 -5.7; 588 -5.3; 647 -4.7; 712 -4.3; 783 -4.1; 861 -4.0; 947 -4.1; 1042 -4.3; 1146 -4.4; 1261 -4.0; 1387 -3.5; 1526 -3.4; 1678 -4.0; 1846 -5.0; 2031 -5.9; 2234 -6.0; 2457 -5.3; 2703 -4.2; 2973 -3.0; 3270 -2.3; 3597 -1.9; 3957 -1.6; 4353 -1.5; 4788 -1.5; 5267 -1.0; 5793 -0.5; 6373 -1.1; 7010 -4.8; 7711 -8.2; 8482 -7.2; 9330 -6.3; 10263 -9.3; 11289 -11.8; 12418 -9.0; 13660 -6.2; 15026 -6.2; 16529 -7.3; 18182 -6.3; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.4  | -6.5 dB |
| Peaking | 112 Hz   | 1.09 | -4.7 dB |
| Peaking | 197 Hz   | 1.96 | -3.3 dB |
| Peaking | 6684 Hz  | 0.41 | 7.3 dB  |
| Peaking | 10355 Hz | 0.95 | -9.5 dB |
| Peaking | 780 Hz   | 1.46 | 1.9 dB  |
| Peaking | 1495 Hz  | 3.05 | 1.7 dB  |
| Peaking | 2213 Hz  | 2.43 | -3.0 dB |
| Peaking | 7323 Hz  | 1.62 | 3.9 dB  |
| Peaking | 7575 Hz  | 4.49 | -7.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%20Sport/Jabra%20Elite%20Sport.png)