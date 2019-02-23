# Sony MDR-Z1R sn3922
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.6; 25 -9.8; 28 -10.0; 31 -10.1; 34 -10.2; 37 -10.2; 41 -10.1; 45 -10.1; 49 -10.0; 54 -9.9; 60 -9.5; 66 -9.2; 72 -9.7; 79 -10.5; 87 -11.2; 96 -11.8; 106 -11.9; 116 -11.8; 128 -12.0; 141 -11.9; 155 -11.0; 170 -10.3; 187 -10.2; 206 -9.5; 227 -8.9; 249 -8.7; 274 -8.3; 302 -8.0; 332 -7.7; 365 -7.4; 402 -7.1; 442 -6.8; 486 -6.6; 535 -6.1; 588 -5.4; 647 -5.3; 712 -5.2; 783 -5.0; 861 -5.1; 947 -5.2; 1042 -5.1; 1146 -4.9; 1261 -5.2; 1387 -5.6; 1526 -6.4; 1678 -7.0; 1846 -7.3; 2031 -7.1; 2234 -6.2; 2457 -5.1; 2703 -2.5; 2973 -3.4; 3270 -8.6; 3597 -3.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -1.5; 6373 -2.6; 7010 -6.1; 7711 -6.2; 8482 -8.1; 9330 -14.3; 10263 -14.4; 11289 -7.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Z1R sn3922 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Z1R sn3922 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.74 | -3.4 dB  |
| Peaking | 123 Hz   | 0.97 | -5.3 dB  |
| Peaking | 4516 Hz  | 1.95 | 6.4 dB   |
| Peaking | 6031 Hz  | 5.76 | 3.2 dB   |
| Peaking | 9757 Hz  | 4.44 | -10.4 dB |
| Peaking | 972 Hz   | 1.03 | 1.8 dB   |
| Peaking | 1927 Hz  | 2.17 | -2.2 dB  |
| Peaking | 2876 Hz  | 4.09 | 5.3 dB   |
| Peaking | 3188 Hz  | 8.43 | -7.7 dB  |
| Peaking | 11860 Hz | 8.21 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-Z1R%20sn3922/Sony%20MDR-Z1R%20sn3922.png)