# Sennheiser Momentum True Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.1; 25 -1.2; 28 -1.2; 31 -1.3; 34 -1.3; 37 -1.3; 41 -1.3; 45 -1.4; 49 -1.4; 54 -1.5; 60 -1.7; 66 -2.1; 72 -2.4; 79 -2.7; 87 -3.1; 96 -3.6; 106 -4.1; 116 -4.5; 128 -5.0; 141 -5.3; 155 -5.5; 170 -5.6; 187 -5.6; 206 -5.6; 227 -5.4; 249 -5.1; 274 -4.7; 302 -4.3; 332 -4.0; 365 -3.6; 402 -3.2; 442 -2.8; 486 -2.4; 535 -1.9; 588 -1.3; 647 -0.7; 712 -0.2; 783 0.2; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.6; 1387 -2.2; 1526 -2.4; 1678 -2.1; 1846 -1.2; 2031 0.0; 2234 1.9; 2457 3.8; 2703 5.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.9; 4353 5.2; 4788 4.9; 5267 4.2; 5793 2.5; 6373 -1.3; 7010 -4.2; 7711 -3.3; 8482 -1.2; 9330 -2.5; 10263 -6.7; 11289 -8.8; 12418 -7.5; 13660 -5.9; 15026 -3.5; 16529 -0.2; 18182 0.0; 20000 -0.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum True Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum True Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 202 Hz   | 0.45 | -5.9 dB  |
| Peaking | 1652 Hz  | 1.15 | -9.9 dB  |
| Peaking | 2789 Hz  | 0.36 | 9.4 dB   |
| Peaking | 6962 Hz  | 3.62 | -7.2 dB  |
| Peaking | 11649 Hz | 1.39 | -10.9 dB |
| Peaking | 24 Hz    | 1.68 | -0.9 dB  |
| Peaking | 2126 Hz  | 6.88 | -0.7 dB  |
| Peaking | 2769 Hz  | 5.44 | 0.8 dB   |
| Peaking | 4278 Hz  | 4.57 | -0.4 dB  |
| Peaking | 16826 Hz | 4.35 | 1.3 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Momentum%20True%20Wireless/Sennheiser%20Momentum%20True%20Wireless.png)