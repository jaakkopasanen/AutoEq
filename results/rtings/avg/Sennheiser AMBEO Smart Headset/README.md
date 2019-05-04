# Sennheiser AMBEO Smart Headset
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.4; 25 -6.2; 28 -7.1; 31 -7.8; 34 -8.3; 37 -8.7; 41 -9.0; 45 -9.3; 49 -9.6; 54 -9.8; 60 -10.1; 66 -10.4; 72 -10.6; 79 -10.9; 87 -11.2; 96 -11.4; 106 -11.6; 116 -11.7; 128 -11.8; 141 -11.7; 155 -11.5; 170 -11.2; 187 -10.9; 206 -10.7; 227 -10.4; 249 -10.1; 274 -9.6; 302 -9.1; 332 -8.5; 365 -7.9; 402 -7.3; 442 -6.7; 486 -6.0; 535 -5.3; 588 -4.6; 647 -3.8; 712 -3.0; 783 -2.4; 861 -2.4; 947 -2.8; 1042 -3.4; 1146 -4.1; 1261 -4.7; 1387 -4.9; 1526 -4.9; 1678 -4.8; 1846 -4.7; 2031 -4.4; 2234 -3.6; 2457 -2.2; 2703 -1.1; 2973 -0.5; 3270 -0.7; 3597 -1.3; 3957 -2.1; 4353 -2.9; 4788 -4.0; 5267 -4.8; 5793 -6.2; 6373 -8.7; 7010 -9.1; 7711 -7.5; 8482 -8.7; 9330 -11.8; 10263 -13.5; 11289 -12.4; 12418 -10.5; 13660 -7.0; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser AMBEO Smart Headset GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser AMBEO Smart Headset ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 56 Hz    | 1.12 | -1.3 dB |
| Peaking | 141 Hz   | 0.51 | -5.3 dB |
| Peaking | 786 Hz   | 1.38 | 4.5 dB  |
| Peaking | 3206 Hz  | 1.52 | 6.2 dB  |
| Peaking | 10396 Hz | 1.77 | -7.5 dB |
| Peaking | 19 Hz    | 3.04 | 2.8 dB  |
| Peaking | 5020 Hz  | 3.06 | 0.9 dB  |
| Peaking | 6637 Hz  | 4.86 | -3.1 dB |
| Peaking | 7990 Hz  | 5.88 | 1.7 dB  |
| Peaking | 14359 Hz | 4.28 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20AMBEO%20Smart%20Headset/Sennheiser%20AMBEO%20Smart%20Headset.png)