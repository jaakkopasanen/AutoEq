# XFYRO xS2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 4.2; 25 3.9; 28 3.4; 31 3.0; 34 2.7; 37 2.4; 41 2.0; 45 1.7; 49 1.4; 54 0.9; 60 0.2; 66 -0.5; 72 -1.0; 79 -1.7; 87 -2.4; 96 -3.2; 106 -4.0; 116 -4.7; 128 -5.4; 141 -6.1; 155 -6.6; 170 -7.0; 187 -7.4; 206 -7.6; 227 -7.6; 249 -7.4; 274 -7.1; 302 -6.7; 332 -6.3; 365 -5.8; 402 -5.3; 442 -4.7; 486 -4.0; 535 -3.1; 588 -2.3; 647 -1.4; 712 -0.7; 783 -0.1; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 0.2; 1387 0.4; 1526 0.6; 1678 1.0; 1846 1.4; 2031 1.9; 2234 3.1; 2457 4.2; 2703 4.1; 2973 2.9; 3270 0.9; 3597 -1.2; 3957 -2.9; 4353 -4.8; 4788 -6.4; 5267 -8.6; 5793 -8.5; 6373 -5.5; 7010 -2.2; 7711 -1.2; 8482 -3.7; 9330 -4.4; 10263 -0.5; 11289 0.0; 12418 0.0; 13660 -0.4; 15026 -8.5; 16529 -14.4; 18182 -13.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`XFYRO xS2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `XFYRO xS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.4  | 4.9 dB   |
| Peaking | 210 Hz   | 0.62 | -8.1 dB  |
| Peaking | 2554 Hz  | 1.8  | 5.2 dB   |
| Peaking | 5293 Hz  | 2.17 | -9.2 dB  |
| Peaking | 17569 Hz | 1.25 | -16.3 dB |
| Peaking | 833 Hz   | 3.27 | 1.6 dB   |
| Peaking | 7426 Hz  | 5.85 | 2.7 dB   |
| Peaking | 9028 Hz  | 6.47 | -3.4 dB  |
| Peaking | 12457 Hz | 1.77 | 5.6 dB   |
| Peaking | 18593 Hz | 0.16 | -2.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/XFYRO%20xS2/XFYRO%20xS2.png)