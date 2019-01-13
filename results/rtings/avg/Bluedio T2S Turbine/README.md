# Bluedio T2S Turbine
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -13.6; 23 -14.2; 25 -14.7; 28 -15.3; 31 -15.5; 34 -15.6; 37 -15.5; 41 -15.4; 45 -15.2; 49 -15.1; 54 -15.0; 60 -14.9; 66 -14.9; 72 -14.9; 79 -14.9; 87 -15.1; 96 -15.2; 106 -15.2; 116 -15.3; 128 -15.5; 141 -15.5; 155 -15.6; 170 -15.5; 187 -15.2; 206 -14.9; 227 -14.7; 249 -14.3; 274 -14.0; 302 -13.5; 332 -12.9; 365 -12.0; 402 -10.7; 442 -9.7; 486 -9.0; 535 -7.9; 588 -6.7; 647 -5.2; 712 -3.4; 783 -1.7; 861 -0.1; 947 0.6; 1042 -1.2; 1146 -2.3; 1261 -1.6; 1387 -2.7; 1526 -2.6; 1678 -3.0; 1846 -3.8; 2031 -4.8; 2234 -5.1; 2457 -4.9; 2703 -4.6; 2973 -4.1; 3270 -2.5; 3597 -0.1; 3957 1.6; 4353 1.2; 4788 0.3; 5267 2.5; 5793 0.7; 6373 -6.4; 7010 -2.6; 7711 0.3; 8482 -0.2; 9330 -5.3; 10263 -5.5; 11289 -2.4; 12418 -1.9; 13660 -2.7; 15026 -1.1; 16529 0.0; 18182 -0.0; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T2S Turbine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T2S Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.17 | -14.9 dB |
| Peaking | 265 Hz   | 0.7  | -7.9 dB  |
| Peaking | 2320 Hz  | 2.27 | -5.3 dB  |
| Peaking | 9899 Hz  | 4.61 | -6.4 dB  |
| Peaking | 13602 Hz | 2.73 | -2.3 dB  |
| Peaking | 509 Hz   | 2.6  | -1.5 dB  |
| Peaking | 885 Hz   | 4.13 | 3.9 dB   |
| Peaking | 3007 Hz  | 5.98 | -2.4 dB  |
| Peaking | 5749 Hz  | 1.53 | 4.2 dB   |
| Peaking | 6465 Hz  | 6.45 | -10.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bluedio%20T2S%20Turbine/Bluedio%20T2S%20Turbine.png)