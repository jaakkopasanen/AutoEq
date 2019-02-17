# Cyberdrive Forte Classic Soprano
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.9; 23 -14.8; 25 -14.6; 28 -14.4; 31 -14.2; 34 -13.9; 37 -13.7; 41 -13.4; 45 -13.2; 49 -12.9; 54 -12.6; 60 -12.3; 66 -12.1; 72 -11.9; 79 -11.7; 87 -11.5; 96 -11.3; 106 -11.0; 116 -10.6; 128 -10.3; 141 -9.9; 155 -9.5; 170 -9.0; 187 -8.5; 206 -8.0; 227 -7.4; 249 -6.9; 274 -6.3; 302 -5.7; 332 -5.1; 365 -4.5; 402 -3.9; 442 -3.2; 486 -2.8; 535 -2.2; 588 -1.5; 647 -1.1; 712 -1.0; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -0.9; 1146 -1.1; 1261 -1.5; 1387 -2.0; 1526 -2.6; 1678 -2.9; 1846 -3.0; 2031 -2.9; 2234 -3.0; 2457 -2.9; 2703 -3.5; 2973 -4.6; 3270 -6.6; 3597 -8.7; 3957 -9.2; 4353 -10.5; 4788 -11.7; 5267 -13.9; 5793 -17.3; 6373 -10.7; 7010 -6.4; 7711 -3.7; 8482 -2.6; 9330 -2.9; 10263 -5.9; 11289 -6.9; 12418 -3.9; 13660 -4.7; 15026 -6.2; 16529 -1.2; 18182 -0.9; 20000 -0.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cyberdrive Forte Classic Soprano GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cyberdrive Forte Classic Soprano ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.17 | -13.6 dB |
| Peaking | 170 Hz   | 0.7  | -3.8 dB  |
| Peaking | 4171 Hz  | 1.51 | -7.7 dB  |
| Peaking | 5748 Hz  | 4.38 | -13.0 dB |
| Peaking | 13028 Hz | 1.06 | -4.3 dB  |
| Peaking | 823 Hz   | 1.97 | 1.4 dB   |
| Peaking | 1664 Hz  | 3.27 | -1.3 dB  |
| Peaking | 8690 Hz  | 3.8  | 2.0 dB   |
| Peaking | 10831 Hz | 6.6  | -3.2 dB  |
| Peaking | 17314 Hz | 3.65 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.4 dB |
| Peaking | 62 Hz    | 1.41 | -7.6 dB  |
| Peaking | 125 Hz   | 1.41 | -7.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -10.5 dB |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cyberdrive%20Forte%20Classic%20Soprano/Cyberdrive%20Forte%20Classic%20Soprano.png)