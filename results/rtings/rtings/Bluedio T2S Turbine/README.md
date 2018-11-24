# Bluedio T2S Turbine

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 -13.6; 23 -14.2; 25 -14.7; 28 -15.3; 31 -15.5; 34 -15.6; 37 -15.5; 41 -15.4; 45 -15.2; 49 -15.1; 54 -15.0; 60 -14.9; 66 -14.9; 72 -14.9; 79 -14.9; 87 -15.1; 96 -15.2; 106 -15.2; 116 -15.3; 128 -15.5; 141 -15.5; 155 -15.6; 170 -15.5; 187 -15.2; 206 -14.9; 227 -14.7; 249 -14.3; 274 -14.0; 302 -13.5; 332 -12.9; 365 -12.0; 402 -10.7; 442 -9.7; 486 -9.0; 535 -7.9; 588 -6.7; 647 -5.2; 712 -3.4; 783 -1.7; 861 -0.1; 947 0.6; 1042 -1.2; 1146 -2.3; 1261 -1.6; 1387 -2.7; 1526 -2.6; 1678 -3.0; 1846 -3.8; 2031 -4.8; 2234 -5.2; 2457 -4.9; 2703 -4.3; 2973 -3.6; 3270 -1.8; 3597 0.9; 3957 2.8; 4353 2.5; 4788 2.1; 5267 5.1; 5793 3.1; 6373 -5.2; 7010 -1.7; 7711 0.3; 8482 -0.1; 9330 -6.7; 10263 -7.3; 11289 -1.6; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bluedio T2S Turbine GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio T2S Turbine ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 40 Hz   | 0.17 | -15.0 dB |
| Peaking | 264 Hz  | 0.7  | -7.9 dB  |
| Peaking | 2405 Hz | 1.82 | -5.6 dB  |
| Peaking | 4534 Hz | 2.14 | 4.4 dB   |
| Peaking | 9880 Hz | 4.98 | -9.1 dB  |
| Peaking | 512 Hz  | 2.8  | -1.5 dB  |
| Peaking | 887 Hz  | 3.92 | 3.9 dB   |
| Peaking | 5548 Hz | 7.3  | 5.4 dB   |
| Peaking | 6499 Hz | 5.09 | -8.6 dB  |
| Peaking | 7451 Hz | 3.84 | 3.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bluedio%20T2S%20Turbine/Bluedio%20T2S%20Turbine.png)