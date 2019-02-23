# Shure SRH840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -1.1; 31 -2.0; 34 -2.9; 37 -3.8; 41 -5.1; 45 -6.3; 49 -7.0; 54 -7.2; 60 -6.9; 66 -7.2; 72 -8.4; 79 -9.7; 87 -10.7; 96 -11.4; 106 -11.8; 116 -11.7; 128 -11.3; 141 -11.1; 155 -10.1; 170 -9.4; 187 -8.7; 206 -7.4; 227 -6.7; 249 -6.3; 274 -5.8; 302 -8.2; 332 -7.8; 365 -7.1; 402 -6.5; 442 -6.2; 486 -5.9; 535 -5.6; 588 -5.1; 647 -4.7; 712 -4.3; 783 -3.8; 861 -3.7; 947 -3.6; 1042 -3.8; 1146 -3.6; 1261 -3.6; 1387 -4.2; 1526 -5.4; 1678 -6.8; 1846 -7.6; 2031 -8.0; 2234 -8.3; 2457 -8.0; 2703 -6.8; 2973 -6.4; 3270 -5.6; 3597 -5.0; 3957 -4.8; 4353 -6.0; 4788 -6.8; 5267 -3.8; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -12.3; 9330 -15.0; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 1.3  | 6.7 dB   |
| Peaking | 111 Hz  | 1.23 | -5.8 dB  |
| Peaking | 920 Hz  | 1.5  | 3.4 dB   |
| Peaking | 6139 Hz | 3.51 | 6.9 dB   |
| Peaking | 9057 Hz | 5.32 | -10.3 dB |
| Peaking | 274 Hz  | 3.51 | 2.3 dB   |
| Peaking | 312 Hz  | 5.27 | -3.0 dB  |
| Peaking | 1325 Hz | 4.25 | 1.9 dB   |
| Peaking | 2110 Hz | 2    | -2.4 dB  |
| Peaking | 3608 Hz | 5.14 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH840/Shure%20SRH840.png)