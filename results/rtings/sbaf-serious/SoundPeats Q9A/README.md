# SoundPeats Q9A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 -5.0; 23 -5.1; 25 -5.2; 28 -5.4; 31 -5.5; 34 -5.6; 37 -5.6; 41 -5.8; 45 -5.8; 49 -5.9; 54 -6.1; 60 -6.4; 66 -6.7; 72 -6.9; 79 -7.0; 87 -7.2; 96 -7.6; 106 -8.1; 116 -8.6; 128 -9.0; 141 -9.5; 155 -9.7; 170 -9.7; 187 -9.7; 206 -9.6; 227 -9.3; 249 -8.7; 274 -8.0; 302 -7.2; 332 -6.4; 365 -5.6; 402 -4.8; 442 -3.9; 486 -2.9; 535 -2.0; 588 -1.1; 647 -0.3; 712 0.1; 783 0.1; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.9; 1387 -2.4; 1526 -4.4; 1678 -6.3; 1846 -7.0; 2031 -6.5; 2234 -4.4; 2457 -1.7; 2703 1.2; 2973 3.4; 3270 4.8; 3597 5.0; 3957 3.3; 4353 0.7; 4788 -0.8; 5267 -1.3; 5793 -0.1; 6373 1.5; 7010 2.1; 7711 -0.5; 8482 -2.1; 9330 -0.1; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q9A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q9A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.29 | -5.4 dB |
| Peaking | 163 Hz  | 0.94 | -6.5 dB |
| Peaking | 287 Hz  | 1.47 | -4.0 dB |
| Peaking | 1891 Hz | 2.64 | -8.1 dB |
| Peaking | 3334 Hz | 3.03 | 6.4 dB  |
| Peaking | 434 Hz  | 3.34 | -1.1 dB |
| Peaking | 766 Hz  | 1.63 | 1.5 dB  |
| Peaking | 5205 Hz | 3.8  | -2.9 dB |
| Peaking | 6861 Hz | 2.25 | 3.2 dB  |
| Peaking | 8319 Hz | 4.57 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/SoundPeats%20Q9A/SoundPeats%20Q9A.png)