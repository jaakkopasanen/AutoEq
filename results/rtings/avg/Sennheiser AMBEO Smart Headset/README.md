# Sennheiser AMBEO Smart Headset
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.6; 25 -2.4; 28 -3.3; 31 -3.9; 34 -4.3; 37 -4.7; 41 -5.0; 45 -5.3; 49 -5.6; 54 -6.0; 60 -6.5; 66 -7.1; 72 -7.5; 79 -8.1; 87 -8.7; 96 -9.3; 106 -9.9; 116 -10.5; 128 -11.0; 141 -11.4; 155 -11.6; 170 -11.6; 187 -11.5; 206 -11.4; 227 -11.4; 249 -11.1; 274 -10.7; 302 -10.1; 332 -9.5; 365 -8.9; 402 -8.3; 442 -7.7; 486 -7.0; 535 -6.3; 588 -5.5; 647 -4.7; 712 -3.9; 783 -3.3; 861 -3.3; 947 -3.6; 1042 -4.2; 1146 -4.9; 1261 -5.5; 1387 -5.7; 1526 -5.7; 1678 -5.5; 1846 -5.4; 2031 -5.0; 2234 -3.7; 2457 -2.3; 2703 -1.5; 2973 -1.4; 3270 -1.9; 3597 -2.6; 3957 -3.3; 4353 -4.2; 4788 -4.6; 5267 -5.4; 5793 -7.2; 6373 -10.6; 7010 -9.8; 7711 -7.7; 8482 -9.9; 9330 -14.4; 10263 -15.0; 11289 -12.4; 12418 -11.2; 13660 -8.5; 15026 -7.1; 16529 -7.1; 18182 -7.1; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser AMBEO Smart Headset GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser AMBEO Smart Headset ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.43 | 8.4 dB  |
| Peaking | 180 Hz   | 0.64 | -5.1 dB |
| Peaking | 788 Hz   | 1.49 | 4.3 dB  |
| Peaking | 3076 Hz  | 1.43 | 6.0 dB  |
| Peaking | 10141 Hz | 1.87 | -8.3 dB |
| Peaking | 5116 Hz  | 3.93 | 1.5 dB  |
| Peaking | 6521 Hz  | 5.14 | -4.0 dB |
| Peaking | 7807 Hz  | 6.38 | 2.8 dB  |
| Peaking | 12954 Hz | 4.78 | -2.1 dB |
| Peaking | 14321 Hz | 2.12 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20AMBEO%20Smart%20Headset/Sennheiser%20AMBEO%20Smart%20Headset.png)