# AUKEY Latitude
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.7dB
GraphicEQ: 21 -0.6; 23 -0.5; 25 -0.4; 28 -0.4; 31 -0.3; 34 -0.3; 37 -0.3; 41 -0.2; 45 -0.3; 49 -0.3; 54 -0.5; 60 -1.0; 66 -1.4; 72 -1.8; 79 -2.3; 87 -2.7; 96 -3.3; 106 -3.9; 116 -4.5; 128 -5.1; 141 -5.5; 155 -5.8; 170 -5.9; 187 -5.9; 206 -6.1; 227 -6.2; 249 -6.0; 274 -5.6; 302 -5.1; 332 -4.7; 365 -4.2; 402 -3.7; 442 -3.1; 486 -2.6; 535 -2.0; 588 -1.3; 647 -0.5; 712 0.1; 783 0.5; 861 0.5; 947 0.3; 1042 -0.3; 1146 -1.0; 1261 -0.9; 1387 -0.9; 1526 -0.7; 1678 -0.4; 1846 -0.1; 2031 0.2; 2234 0.5; 2457 0.4; 2703 -0.2; 2973 -1.8; 3270 -3.7; 3597 -4.9; 3957 -4.7; 4353 -4.6; 4788 -4.2; 5267 -4.4; 5793 -4.8; 6373 -5.2; 7010 -4.7; 7711 -2.0; 8482 -1.5; 9330 -5.6; 10263 -9.3; 11289 -6.2; 12418 -0.5; 13660 0.0; 15026 -0.3; 16529 -5.0; 18182 -6.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AUKEY Latitude GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-7**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AUKEY Latitude ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 197 Hz   | 0.68 | -6.5 dB |
| Peaking | 4987 Hz  | 1.2  | -5.1 dB |
| Peaking | 10373 Hz | 4.4  | -9.3 dB |
| Peaking | 17819 Hz | 1.89 | -7.3 dB |
| Peaking | 22049 Hz | 1.77 | -6.7 dB |
| Peaking | 797 Hz   | 3.81 | 1.7 dB  |
| Peaking | 2429 Hz  | 2.92 | 2.0 dB  |
| Peaking | 3474 Hz  | 5.18 | -2.4 dB |
| Peaking | 11373 Hz | 6.24 | -2.2 dB |
| Peaking | 13048 Hz | 2.31 | 2.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AUKEY%20Latitude/AUKEY%20Latitude.png)