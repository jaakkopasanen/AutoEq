# Piaton Moderna MS200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -6.1; 25 -6.7; 28 -7.5; 31 -8.2; 34 -8.8; 37 -9.3; 41 -10.0; 45 -10.6; 49 -11.1; 54 -11.7; 60 -12.3; 66 -12.9; 72 -13.4; 79 -14.0; 87 -14.5; 96 -15.2; 106 -15.5; 116 -15.7; 128 -16.0; 141 -16.4; 155 -16.5; 170 -16.5; 187 -16.6; 206 -16.5; 227 -16.3; 249 -16.2; 274 -15.9; 302 -15.5; 332 -15.1; 365 -14.7; 402 -13.9; 442 -12.9; 486 -13.0; 535 -12.5; 588 -11.4; 647 -10.4; 712 -9.4; 783 -8.3; 861 -7.5; 947 -6.8; 1042 -6.4; 1146 -6.1; 1261 -6.1; 1387 -7.0; 1526 -8.3; 1678 -9.0; 1846 -9.8; 2031 -10.0; 2234 -10.0; 2457 -8.4; 2703 -6.1; 2973 -3.3; 3270 -1.2; 3597 -0.5; 3957 -1.0; 4353 -3.5; 4788 -4.7; 5267 -4.2; 5793 -4.7; 6373 -7.4; 7010 -9.0; 7711 -9.9; 8482 -10.2; 9330 -9.8; 10263 -8.9; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Piaton Moderna MS200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Piaton Moderna MS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 140 Hz  | 0.43 | -9.0 dB  |
| Peaking | 426 Hz  | 0.66 | -5.0 dB  |
| Peaking | 2164 Hz | 1.01 | -17.5 dB |
| Peaking | 2991 Hz | 0.4  | 16.8 dB  |
| Peaking | 7653 Hz | 0.88 | -10.2 dB |
| Peaking | 21 Hz   | 2.44 | 2.4 dB   |
| Peaking | 2681 Hz | 5.96 | -1.2 dB  |
| Peaking | 3731 Hz | 2.53 | 2.0 dB   |
| Peaking | 4560 Hz | 3.42 | -3.0 dB  |
| Peaking | 5641 Hz | 6.04 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.9 dB |
| Peaking | 250 Hz   | 1.41 | -8.2 dB |
| Peaking | 500 Hz   | 1.41 | -5.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Piaton%20Moderna%20MS200/Piaton%20Moderna%20MS200.png)