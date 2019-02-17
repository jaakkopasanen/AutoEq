# Bluedio T2S Turbine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.6; 23 -17.2; 25 -17.7; 28 -18.2; 31 -18.5; 34 -18.6; 37 -18.5; 41 -18.4; 45 -18.2; 49 -18.1; 54 -18.0; 60 -17.9; 66 -17.9; 72 -17.9; 79 -17.9; 87 -18.0; 96 -18.1; 106 -18.2; 116 -18.3; 128 -18.4; 141 -18.5; 155 -18.6; 170 -18.5; 187 -18.2; 206 -17.9; 227 -17.6; 249 -17.3; 274 -17.0; 302 -16.5; 332 -15.9; 365 -15.0; 402 -13.7; 442 -12.7; 486 -12.0; 535 -10.9; 588 -9.6; 647 -8.2; 712 -6.4; 783 -4.6; 861 -3.1; 947 -2.3; 1042 -4.2; 1146 -5.3; 1261 -4.6; 1387 -5.7; 1526 -5.6; 1678 -6.0; 1846 -6.8; 2031 -7.8; 2234 -8.1; 2457 -7.9; 2703 -7.5; 2973 -7.0; 3270 -5.5; 3597 -3.1; 3957 -1.4; 4353 -1.8; 4788 -2.6; 5267 -0.5; 5793 -2.3; 6373 -9.4; 7010 -5.6; 7711 -2.7; 8482 -3.2; 9330 -8.3; 10263 -8.5; 11289 -5.4; 12418 -4.8; 13660 -5.6; 15026 -4.1; 16529 -3.0; 18182 -3.0; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T2S Turbine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T2S Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.17 | -14.9 dB |
| Peaking | 264 Hz   | 0.7  | -7.9 dB  |
| Peaking | 2320 Hz  | 2.26 | -5.3 dB  |
| Peaking | 9913 Hz  | 4.25 | -6.4 dB  |
| Peaking | 13644 Hz | 2.69 | -2.4 dB  |
| Peaking | 512 Hz   | 2.93 | -1.4 dB  |
| Peaking | 886 Hz   | 4.12 | 3.9 dB   |
| Peaking | 3020 Hz  | 5.95 | -2.4 dB  |
| Peaking | 5817 Hz  | 1.5  | 4.3 dB   |
| Peaking | 6434 Hz  | 6.22 | -10.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -15.8 dB |
| Peaking | 62 Hz    | 1.41 | -9.7 dB  |
| Peaking | 125 Hz   | 1.41 | -11.6 dB |
| Peaking | 250 Hz   | 1.41 | -12.1 dB |
| Peaking | 500 Hz   | 1.41 | -6.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T2S%20Turbine/Bluedio%20T2S%20Turbine.png)