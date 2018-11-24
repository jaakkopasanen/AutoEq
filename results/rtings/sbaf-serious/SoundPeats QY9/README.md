# SoundPeats QY9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.2; 25 3.6; 28 3.0; 31 2.3; 34 1.8; 37 1.3; 41 0.7; 45 0.3; 49 -0.2; 54 -0.8; 60 -1.5; 66 -2.2; 72 -2.6; 79 -3.2; 87 -3.8; 96 -4.6; 106 -5.5; 116 -6.3; 128 -7.1; 141 -7.7; 155 -8.2; 170 -8.7; 187 -9.3; 206 -9.6; 227 -9.7; 249 -9.4; 274 -9.0; 302 -8.4; 332 -7.8; 365 -7.1; 402 -6.4; 442 -5.5; 486 -4.4; 535 -3.2; 588 -2.1; 647 -0.9; 712 -0.3; 783 -0.4; 861 -0.6; 947 -0.4; 1042 0.4; 1146 1.3; 1261 1.8; 1387 2.0; 1526 2.8; 1678 4.0; 1846 5.7; 2031 6.0; 2234 6.0; 2457 6.0; 2703 5.5; 2973 3.6; 3270 3.6; 3597 3.4; 3957 1.3; 4353 -1.5; 4788 -2.3; 5267 -2.1; 5793 -2.0; 6373 -1.7; 7010 0.0; 7711 -0.2; 8482 -2.7; 9330 -2.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats QY9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats QY9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 19 Hz   |  0.78 | 5.1 dB   |
| Peaking | 212 Hz  |  0.58 | -10.0 dB |
| Peaking | 2352 Hz |  0.83 | 6.7 dB   |
| Peaking | 4968 Hz |  1.98 | -4.8 dB  |
| Peaking | 8785 Hz |  7.1  | -3.5 dB  |
| Peaking | 396 Hz  |  1.84 | -1.2 dB  |
| Peaking | 681 Hz  |  3.23 | 1.7 dB   |
| Peaking | 1006 Hz |  0.41 | 1.7 dB   |
| Peaking | 1071 Hz |  0.77 | -2.2 dB  |
| Peaking | 2996 Hz | 10    | -1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/SoundPeats%20QY9/SoundPeats%20QY9.png)