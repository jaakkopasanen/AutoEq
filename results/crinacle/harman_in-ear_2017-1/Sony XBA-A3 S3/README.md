# Sony XBA-A3 S3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.9; 25 -8.1; 28 -8.3; 31 -8.5; 34 -8.6; 37 -8.7; 41 -8.9; 45 -9.1; 49 -9.2; 54 -9.3; 60 -9.6; 66 -9.8; 72 -10.0; 79 -10.3; 87 -10.6; 96 -10.9; 106 -11.1; 116 -11.3; 128 -11.5; 141 -11.5; 155 -11.5; 170 -11.3; 187 -11.2; 206 -11.0; 227 -10.6; 249 -10.3; 274 -9.9; 302 -9.4; 332 -9.0; 365 -8.6; 402 -8.4; 442 -8.1; 486 -7.9; 535 -7.4; 588 -7.2; 647 -6.9; 712 -6.5; 783 -6.2; 861 -6.0; 947 -6.0; 1042 -6.4; 1146 -6.9; 1261 -7.3; 1387 -7.3; 1526 -6.8; 1678 -6.1; 1846 -5.4; 2031 -4.4; 2234 -3.2; 2457 -2.1; 2703 -1.5; 2973 -1.5; 3270 -1.2; 3597 -2.1; 3957 -2.7; 4353 -4.3; 4788 -5.6; 5267 -3.7; 5793 -0.5; 6373 -0.7; 7010 -3.6; 7711 -5.9; 8482 -6.1; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -7.8; 13660 -16.2; 15026 -23.1; 16529 -25.4; 18182 -23.0; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-A3 S3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-A3 S3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.71 | -1.4 dB  |
| Peaking | 147 Hz   | 0.49 | -5.2 dB  |
| Peaking | 2948 Hz  | 2.06 | 4.3 dB   |
| Peaking | 10382 Hz | 0.46 | 12.2 dB  |
| Peaking | 16240 Hz | 0.57 | -26.8 dB |
| Peaking | 1387 Hz  | 3.8  | -1.8 dB  |
| Peaking | 4909 Hz  | 4.28 | -4.5 dB  |
| Peaking | 6114 Hz  | 1.94 | 7.4 dB   |
| Peaking | 7594 Hz  | 1.62 | -5.1 dB  |
| Peaking | 11963 Hz | 5.61 | 3.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 16000 Hz | 1.41 | -23.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20XBA-A3%20S3/Sony%20XBA-A3%20S3.png)