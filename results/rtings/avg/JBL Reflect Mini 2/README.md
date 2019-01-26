# JBL Reflect Mini 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 21 -2.4; 23 -2.1; 25 -1.9; 28 -1.6; 31 -1.4; 34 -1.3; 37 -1.2; 41 -1.0; 45 -1.0; 49 -1.0; 54 -1.1; 60 -1.4; 66 -1.7; 72 -2.0; 79 -2.3; 87 -2.6; 96 -3.0; 106 -3.4; 116 -3.8; 128 -4.2; 141 -4.4; 155 -4.5; 170 -4.5; 187 -4.4; 206 -4.4; 227 -4.3; 249 -4.0; 274 -3.5; 302 -3.1; 332 -2.6; 365 -2.2; 402 -1.8; 442 -1.3; 486 -0.8; 535 -0.2; 588 0.3; 647 0.8; 712 1.1; 783 1.2; 861 1.1; 947 0.5; 1042 -0.4; 1146 -1.3; 1261 -2.0; 1387 -2.4; 1526 -2.5; 1678 -2.6; 1846 -2.8; 2031 -3.2; 2234 -4.1; 2457 -5.1; 2703 -4.7; 2973 -2.9; 3270 -1.5; 3597 -0.9; 3957 -0.9; 4353 -1.1; 4788 -0.5; 5267 0.0; 5793 -0.2; 6373 -3.0; 7010 -7.9; 7711 -7.8; 8482 -2.9; 9330 -0.0; 10263 -1.1; 11289 -5.3; 12418 -7.9; 13660 -4.9; 15026 -1.8; 16529 -5.0; 18182 -8.5; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Reflect Mini 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-12**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Reflect Mini 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 163 Hz   | 0.71 | -4.8 dB |
| Peaking | 2356 Hz  | 1.86 | -4.8 dB |
| Peaking | 7340 Hz  | 5.47 | -9.3 dB |
| Peaking | 12424 Hz | 3.74 | -7.8 dB |
| Peaking | 18268 Hz | 1.28 | -9.1 dB |
| Peaking | 21 Hz    | 1.35 | -2.3 dB |
| Peaking | 779 Hz   | 1.98 | 2.3 dB  |
| Peaking | 1394 Hz  | 1.96 | -1.9 dB |
| Peaking | 1956 Hz  | 2.09 | 0.7 dB  |
| Peaking | 11241 Hz | 3.82 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Reflect%20Mini%202/JBL%20Reflect%20Mini%202.png)