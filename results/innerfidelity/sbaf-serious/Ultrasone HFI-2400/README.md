# Ultrasone HFI-2400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.6; 25 -2.5; 28 -3.8; 31 -5.0; 34 -6.0; 37 -7.0; 41 -8.0; 45 -8.7; 49 -9.2; 54 -9.9; 60 -10.1; 66 -10.1; 72 -11.0; 79 -11.5; 87 -11.8; 96 -11.9; 106 -11.8; 116 -11.5; 128 -11.4; 141 -11.1; 155 -10.8; 170 -10.3; 187 -9.8; 206 -9.4; 227 -9.5; 249 -10.2; 274 -9.5; 302 -8.8; 332 -8.5; 365 -8.0; 402 -7.6; 442 -7.2; 486 -6.9; 535 -6.5; 588 -5.6; 647 -6.0; 712 -6.4; 783 -6.2; 861 -6.4; 947 -6.7; 1042 -6.7; 1146 -6.7; 1261 -6.7; 1387 -6.8; 1526 -7.1; 1678 -7.2; 1846 -7.6; 2031 -6.3; 2234 -2.0; 2457 -0.8; 2703 -2.8; 2973 -4.7; 3270 -7.5; 3597 -8.7; 3957 -8.2; 4353 -8.0; 4788 -3.3; 5267 -2.3; 5793 -7.3; 6373 -15.8; 7010 -11.2; 7711 -6.5; 8482 -6.8; 9330 -6.8; 10263 -6.8; 11289 -6.8; 12418 -7.2; 13660 -11.5; 15026 -14.9; 16529 -14.3; 18182 -10.6; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-2400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-2400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.25 | 7.3 dB   |
| Peaking | 97 Hz    | 0.55 | -5.2 dB  |
| Peaking | 2478 Hz  | 4.38 | 6.9 dB   |
| Peaking | 3535 Hz  | 5.29 | -2.5 dB  |
| Peaking | 15933 Hz | 1.51 | -9.1 dB  |
| Peaking | 608 Hz   | 2.93 | 1.6 dB   |
| Peaking | 1811 Hz  | 5.99 | -1.8 dB  |
| Peaking | 5227 Hz  | 5.67 | 6.6 dB   |
| Peaking | 6432 Hz  | 5.88 | -10.8 dB |
| Peaking | 9577 Hz  | 1.23 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -8.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20HFI-2400/Ultrasone%20HFI-2400.png)