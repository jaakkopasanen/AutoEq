# Shure SRH840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.9; 28 -3.4; 31 -4.5; 34 -5.4; 37 -6.2; 41 -7.5; 45 -8.8; 49 -9.5; 54 -9.6; 60 -9.4; 66 -9.7; 72 -10.8; 79 -12.1; 87 -13.2; 96 -13.9; 106 -14.2; 116 -14.1; 128 -13.8; 141 -13.5; 155 -12.6; 170 -11.8; 187 -11.2; 206 -9.9; 227 -9.1; 249 -8.8; 274 -8.3; 302 -10.7; 332 -10.3; 365 -9.5; 402 -9.0; 442 -8.7; 486 -8.4; 535 -8.0; 588 -7.6; 647 -7.2; 712 -6.7; 783 -6.3; 861 -6.1; 947 -6.1; 1042 -6.2; 1146 -6.0; 1261 -6.0; 1387 -6.6; 1526 -7.8; 1678 -9.2; 1846 -10.0; 2031 -10.5; 2234 -10.7; 2457 -10.5; 2703 -9.2; 2973 -8.9; 3270 -8.1; 3597 -7.4; 3957 -7.3; 4353 -8.4; 4788 -9.3; 5267 -6.2; 5793 -2.7; 6373 -2.7; 7010 -3.8; 7711 -7.6; 8482 -14.7; 9330 -17.5; 10263 -8.6; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.24 | 6.6 dB   |
| Peaking | 113 Hz   | 0.62 | -7.7 dB  |
| Peaking | 2287 Hz  | 1.64 | -4.6 dB  |
| Peaking | 6488 Hz  | 3.91 | 5.6 dB   |
| Peaking | 9034 Hz  | 4.73 | -13.1 dB |
| Peaking | 260 Hz   | 2.04 | 4.9 dB   |
| Peaking | 301 Hz   | 1.6  | -4.7 dB  |
| Peaking | 1048 Hz  | 1.89 | 1.3 dB   |
| Peaking | 4656 Hz  | 9.06 | -3.6 dB  |
| Peaking | 11007 Hz | 7.24 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH840/Shure%20SRH840.png)