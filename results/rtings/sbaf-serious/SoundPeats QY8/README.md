# SoundPeats QY8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 21 -5.8; 23 -5.8; 25 -5.7; 28 -5.6; 31 -5.5; 34 -5.4; 37 -5.2; 41 -5.0; 45 -4.7; 49 -4.5; 54 -4.3; 60 -4.2; 66 -4.1; 72 -3.9; 79 -3.7; 87 -3.6; 96 -3.6; 106 -3.7; 116 -3.8; 128 -4.3; 141 -5.0; 155 -5.2; 170 -5.0; 187 -4.6; 206 -4.2; 227 -3.8; 249 -3.2; 274 -2.6; 302 -1.9; 332 -1.3; 365 -0.8; 402 -0.2; 442 0.3; 486 0.9; 535 1.5; 588 2.0; 647 2.6; 712 2.6; 783 2.1; 861 1.5; 947 0.5; 1042 -0.4; 1146 -1.2; 1261 -1.8; 1387 -2.5; 1526 -3.3; 1678 -4.0; 1846 -5.1; 2031 -6.5; 2234 -6.8; 2457 -6.4; 2703 -5.4; 2973 -3.7; 3270 -2.5; 3597 -2.8; 3957 -5.6; 4353 -9.6; 4788 -9.0; 5267 -3.5; 5793 1.1; 6373 1.8; 7010 0.4; 7711 -3.2; 8482 -4.1; 9330 -3.4; 10263 -2.8; 11289 -0.2; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats QY8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats QY8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.5  | -5.6 dB  |
| Peaking | 80 Hz   | 0.94 | -1.4 dB  |
| Peaking | 172 Hz  | 1.5  | -4.6 dB  |
| Peaking | 2198 Hz | 1.92 | -7.1 dB  |
| Peaking | 4500 Hz | 4.97 | -10.4 dB |
| Peaking | 277 Hz  | 2.49 | -1.1 dB  |
| Peaking | 693 Hz  | 1.46 | 3.3 dB   |
| Peaking | 1312 Hz | 1.79 | -1.3 dB  |
| Peaking | 6344 Hz | 4.29 | 4.8 dB   |
| Peaking | 8508 Hz | 2.33 | -4.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/SoundPeats%20QY8/SoundPeats%20QY8.png)