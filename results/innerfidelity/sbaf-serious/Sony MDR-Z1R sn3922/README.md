# Sony MDR-Z1R sn3922
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.9; 25 -11.1; 28 -11.3; 31 -11.4; 34 -11.5; 37 -11.5; 41 -11.4; 45 -11.4; 49 -11.3; 54 -11.1; 60 -10.8; 66 -10.5; 72 -11.0; 79 -11.8; 87 -12.5; 96 -13.1; 106 -13.2; 116 -13.1; 128 -13.3; 141 -13.1; 155 -12.2; 170 -11.6; 187 -11.5; 206 -10.8; 227 -10.2; 249 -9.9; 274 -9.6; 302 -9.2; 332 -9.0; 365 -8.7; 402 -8.3; 442 -8.0; 486 -7.9; 535 -7.3; 588 -6.7; 647 -6.6; 712 -6.5; 783 -6.3; 861 -6.4; 947 -6.4; 1042 -6.4; 1146 -6.2; 1261 -6.4; 1387 -6.9; 1526 -7.7; 1678 -8.3; 1846 -8.6; 2031 -8.4; 2234 -7.5; 2457 -6.4; 2703 -3.8; 2973 -4.6; 3270 -9.9; 3597 -4.6; 3957 -0.5; 4353 -0.5; 4788 -1.6; 5267 -2.6; 5793 -2.7; 6373 -3.8; 7010 -7.4; 7711 -6.1; 8482 -9.4; 9330 -15.6; 10263 -15.6; 11289 -8.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z1R sn3922 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1R sn3922 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.81 | -4.3 dB  |
| Peaking | 126 Hz   | 0.65 | -6.3 dB  |
| Peaking | 1873 Hz  | 3.35 | -2.7 dB  |
| Peaking | 4640 Hz  | 1.99 | 6.3 dB   |
| Peaking | 9762 Hz  | 4.24 | -11.8 dB |
| Peaking | 2871 Hz  | 6.65 | 6.2 dB   |
| Peaking | 3203 Hz  | 4.76 | -7.4 dB  |
| Peaking | 3756 Hz  | 8.36 | 3.0 dB   |
| Peaking | 3979 Hz  | 7.09 | 1.3 dB   |
| Peaking | 11987 Hz | 7.21 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-Z1R%20sn3922/Sony%20MDR-Z1R%20sn3922.png)