# AKG K490-NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.1; 34 -1.5; 37 -1.9; 41 -2.4; 45 -2.7; 49 -3.1; 54 -3.6; 60 -4.3; 66 -5.0; 72 -5.7; 79 -6.3; 87 -7.1; 96 -7.8; 106 -8.6; 116 -9.4; 128 -10.0; 141 -10.4; 155 -10.7; 170 -10.9; 187 -10.8; 206 -10.6; 227 -10.7; 249 -10.9; 274 -11.2; 302 -11.3; 332 -11.5; 365 -12.2; 402 -12.5; 442 -12.6; 486 -12.8; 535 -12.9; 588 -12.9; 647 -12.6; 712 -11.9; 783 -10.8; 861 -9.1; 947 -7.2; 1042 -6.5; 1146 -7.7; 1261 -9.2; 1387 -10.6; 1526 -11.0; 1678 -10.5; 1846 -9.0; 2031 -7.5; 2234 -7.1; 2457 -6.6; 2703 -6.6; 2973 -8.2; 3270 -9.9; 3597 -11.5; 3957 -10.1; 4353 -6.2; 4788 -3.5; 5267 -7.4; 5793 -8.0; 6373 -3.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -11.7; 12418 -17.5; 13660 -17.3; 15026 -14.0; 16529 -15.9; 18182 -17.6; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K490-NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K490-NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.55 | 6.3 dB   |
| Peaking | 324 Hz   | 0.37 | -5.9 dB  |
| Peaking | 1568 Hz  | 4.96 | -3.3 dB  |
| Peaking | 13031 Hz | 3.26 | -10.8 dB |
| Peaking | 17654 Hz | 1.19 | -12.0 dB |
| Peaking | 2772 Hz  | 1.31 | 5.1 dB   |
| Peaking | 3776 Hz  | 1.17 | -9.0 dB  |
| Peaking | 4632 Hz  | 4.7  | 8.7 dB   |
| Peaking | 6707 Hz  | 5.05 | 5.9 dB   |
| Peaking | 9712 Hz  | 3.84 | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB   |
| Peaking | 62 Hz    | 1.41 | 1.7 dB   |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -6.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -15.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K490-NC/AKG%20K490-NC.png)