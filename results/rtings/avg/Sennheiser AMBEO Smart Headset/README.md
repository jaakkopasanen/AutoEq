# Sennheiser AMBEO Smart Headset
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.3; 28 -3.2; 31 -3.8; 34 -4.3; 37 -4.6; 41 -5.0; 45 -5.3; 49 -5.5; 54 -5.9; 60 -6.5; 66 -7.0; 72 -7.5; 79 -8.0; 87 -8.6; 96 -9.2; 106 -9.8; 116 -10.4; 128 -10.9; 141 -11.3; 155 -11.5; 170 -11.5; 187 -11.4; 206 -11.4; 227 -11.3; 249 -11.0; 274 -10.6; 302 -10.1; 332 -9.5; 365 -8.9; 402 -8.3; 442 -7.6; 486 -7.0; 535 -6.2; 588 -5.4; 647 -4.6; 712 -3.8; 783 -3.2; 861 -3.2; 947 -3.6; 1042 -4.2; 1146 -4.8; 1261 -5.4; 1387 -5.6; 1526 -5.6; 1678 -5.5; 1846 -5.3; 2031 -4.9; 2234 -3.7; 2457 -2.2; 2703 -1.4; 2973 -1.4; 3270 -1.8; 3597 -2.5; 3957 -3.3; 4353 -4.2; 4788 -4.5; 5267 -5.3; 5793 -7.1; 6373 -10.5; 7010 -9.8; 7711 -7.6; 8482 -9.9; 9330 -14.4; 10263 -14.9; 11289 -12.3; 12418 -11.2; 13660 -8.5; 15026 -4.0; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser AMBEO Smart Headset GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser AMBEO Smart Headset ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 1.95 | 4.4 dB   |
| Peaking | 176 Hz   | 0.56 | -8.0 dB  |
| Peaking | 3039 Hz  | 2.76 | 3.4 dB   |
| Peaking | 6511 Hz  | 6.3  | -5.1 dB  |
| Peaking | 10318 Hz | 1.62 | -11.3 dB |
| Peaking | 818 Hz   | 2.47 | 2.6 dB   |
| Peaking | 1594 Hz  | 1.32 | -1.8 dB  |
| Peaking | 2508 Hz  | 4.66 | 1.5 dB   |
| Peaking | 13144 Hz | 3.76 | -4.1 dB  |
| Peaking | 14487 Hz | 1.22 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB   |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB  |
| Peaking | 250 Hz   | 1.41 | -6.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20AMBEO%20Smart%20Headset/Sennheiser%20AMBEO%20Smart%20Headset.png)