# Howard Leight Sync
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.8; 96 -2.9; 106 -5.4; 116 -7.5; 128 -9.3; 141 -9.9; 155 -10.8; 170 -10.3; 187 -10.8; 206 -10.2; 227 -9.7; 249 -9.3; 274 -8.8; 302 -7.9; 332 -6.4; 365 -5.7; 402 -5.4; 442 -4.3; 486 -4.5; 535 -4.2; 588 -3.7; 647 -3.5; 712 -3.0; 783 -2.1; 861 -1.1; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -1.2; 1678 -4.5; 1846 -7.8; 2031 -10.6; 2234 -12.8; 2457 -10.0; 2703 -9.1; 2973 -7.2; 3270 -1.5; 3597 -0.5; 3957 -1.5; 4353 -1.3; 4788 -2.8; 5267 -6.7; 5793 -13.0; 6373 -15.0; 7010 -12.5; 7711 -11.7; 8482 -14.2; 9330 -16.6; 10263 -15.6; 11289 -12.3; 12418 -10.8; 13660 -12.9; 15026 -13.8; 16529 -10.2; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Howard Leight Sync GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Howard Leight Sync ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.91 | 7.4 dB   |
| Peaking | 1033 Hz  | 1.56 | 7.0 dB   |
| Peaking | 9248 Hz  | 1.61 | -9.7 dB  |
| Peaking | 14858 Hz | 2.06 | -6.7 dB  |
| Peaking | 22050 Hz | 1.97 | -8.2 dB  |
| Peaking | 83 Hz    | 2.33 | 5.3 dB   |
| Peaking | 160 Hz   | 1.2  | -5.8 dB  |
| Peaking | 2348 Hz  | 2.1  | -13.4 dB |
| Peaking | 3580 Hz  | 0.67 | 9.6 dB   |
| Peaking | 6158 Hz  | 3.45 | -11.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB   |
| Peaking | 62 Hz    | 1.41 | 7.6 dB   |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 8.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -11.0 dB |
| Peaking | 16000 Hz | 1.41 | -6.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Howard%20Leight%20Sync/Howard%20Leight%20Sync.png)