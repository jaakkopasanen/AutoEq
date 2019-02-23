# Sony MDR-Z1R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.9; 25 -9.0; 28 -9.2; 31 -9.2; 34 -9.3; 37 -9.4; 41 -9.4; 45 -9.2; 49 -9.0; 54 -9.0; 60 -9.1; 66 -9.3; 72 -9.4; 79 -9.6; 87 -10.2; 96 -10.9; 106 -11.1; 116 -11.2; 128 -11.5; 141 -11.5; 155 -11.2; 170 -10.4; 187 -10.0; 206 -9.5; 227 -9.0; 249 -8.5; 274 -8.1; 302 -7.7; 332 -7.3; 365 -7.0; 402 -6.8; 442 -6.7; 486 -6.5; 535 -5.9; 588 -5.9; 647 -6.1; 712 -6.2; 783 -6.3; 861 -6.4; 947 -6.1; 1042 -5.7; 1146 -5.1; 1261 -4.8; 1387 -4.7; 1526 -4.9; 1678 -5.5; 1846 -6.4; 2031 -7.3; 2234 -7.2; 2457 -7.4; 2703 -5.7; 2973 -4.6; 3270 -11.1; 3597 -5.6; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -2.5; 5793 -0.7; 6373 -3.2; 7010 -6.5; 7711 -6.2; 8482 -6.5; 9330 -7.7; 10263 -10.8; 11289 -10.0; 12418 -9.0; 13660 -10.0; 15026 -10.9; 16529 -7.9; 18182 -6.5; 20000 -15.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.55 | -2.5 dB |
| Peaking | 133 Hz   | 1    | -4.8 dB |
| Peaking | 1296 Hz  | 3.16 | 2.0 dB  |
| Peaking | 5097 Hz  | 1.85 | 6.9 dB  |
| Peaking | 13067 Hz | 0.62 | -3.9 dB |
| Peaking | 568 Hz   | 2.86 | 0.9 dB  |
| Peaking | 2192 Hz  | 5.37 | -1.6 dB |
| Peaking | 3330 Hz  | 9.83 | -7.3 dB |
| Peaking | 3935 Hz  | 6.26 | 4.0 dB  |
| Peaking | 17249 Hz | 4.92 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -4.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sony%20MDR-Z1R/Sony%20MDR-Z1R.png)