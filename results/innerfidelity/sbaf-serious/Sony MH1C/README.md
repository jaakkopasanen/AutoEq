# Sony MH1C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.3; 23 -17.2; 25 -17.0; 28 -16.8; 31 -16.6; 34 -16.4; 37 -16.2; 41 -15.9; 45 -15.7; 49 -15.5; 54 -15.2; 60 -15.0; 66 -14.8; 72 -14.6; 79 -14.5; 87 -14.3; 96 -14.2; 106 -13.9; 116 -13.5; 128 -13.3; 141 -13.0; 155 -12.6; 170 -12.2; 187 -11.8; 206 -11.4; 227 -10.9; 249 -10.5; 274 -9.9; 302 -9.4; 332 -9.0; 365 -8.5; 402 -8.0; 442 -7.5; 486 -7.2; 535 -6.9; 588 -6.3; 647 -6.1; 712 -6.0; 783 -5.8; 861 -6.1; 947 -6.5; 1042 -6.5; 1146 -7.6; 1261 -7.6; 1387 -7.9; 1526 -8.6; 1678 -9.2; 1846 -9.3; 2031 -9.2; 2234 -9.2; 2457 -8.6; 2703 -8.1; 2973 -6.8; 3270 -5.0; 3597 -3.7; 3957 -3.3; 4353 -4.1; 4788 -3.2; 5267 -1.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.9; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH1C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH1C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.19 | -10.5 dB |
| Peaking | 156 Hz   | 0.8  | -3.1 dB  |
| Peaking | 2078 Hz  | 1.57 | -3.4 dB  |
| Peaking | 3712 Hz  | 3.18 | 3.2 dB   |
| Peaking | 5842 Hz  | 3.01 | 6.6 dB   |
| Peaking | 320 Hz   | 1.43 | -0.8 dB  |
| Peaking | 899 Hz   | 0.81 | 2.0 dB   |
| Peaking | 1252 Hz  | 1.35 | -1.8 dB  |
| Peaking | 8068 Hz  | 4.93 | -1.1 dB  |
| Peaking | 15268 Hz | 4.76 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MH1C/Sony%20MH1C.png)