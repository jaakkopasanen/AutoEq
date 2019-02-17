# Ultrasone HFI-2400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.6; 25 -2.5; 28 -3.8; 31 -5.0; 34 -6.0; 37 -7.0; 41 -8.0; 45 -8.7; 49 -9.2; 54 -9.9; 60 -10.1; 66 -10.1; 72 -11.0; 79 -11.5; 87 -11.8; 96 -11.9; 106 -11.8; 116 -11.5; 128 -11.4; 141 -11.1; 155 -10.8; 170 -10.3; 187 -9.8; 206 -9.4; 227 -9.5; 249 -10.2; 274 -9.5; 302 -8.8; 332 -8.5; 365 -8.0; 402 -7.6; 442 -7.2; 486 -6.9; 535 -6.5; 588 -5.6; 647 -6.0; 712 -6.4; 783 -6.2; 861 -6.4; 947 -6.7; 1042 -6.7; 1146 -6.7; 1261 -6.7; 1387 -6.8; 1526 -7.1; 1678 -7.2; 1846 -7.6; 2031 -6.3; 2234 -1.9; 2457 -0.5; 2703 -2.8; 2973 -4.7; 3270 -7.5; 3597 -8.7; 3957 -8.2; 4353 -8.0; 4788 -3.3; 5267 -2.3; 5793 -7.3; 6373 -15.8; 7010 -11.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -11.5; 15026 -14.9; 16529 -14.3; 18182 -10.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-2400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-2400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.16 | 7.2 dB   |
| Peaking | 95 Hz    | 0.48 | -5.5 dB  |
| Peaking | 2471 Hz  | 4.95 | 7.0 dB   |
| Peaking | 3567 Hz  | 4.69 | -2.7 dB  |
| Peaking | 15957 Hz | 1.45 | -9.4 dB  |
| Peaking | 598 Hz   | 4.04 | 1.5 dB   |
| Peaking | 1802 Hz  | 5.33 | -1.9 dB  |
| Peaking | 5230 Hz  | 5.71 | 6.5 dB   |
| Peaking | 6435 Hz  | 5.67 | -11.2 dB |
| Peaking | 9340 Hz  | 1.21 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -9.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20HFI-2400/Ultrasone%20HFI-2400.png)