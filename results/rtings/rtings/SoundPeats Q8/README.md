# SoundPeats Q8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.3dB
GraphicEQ: 21 -8.1; 23 -8.4; 25 -8.6; 28 -8.9; 31 -9.0; 34 -9.1; 37 -9.2; 41 -9.2; 45 -9.1; 49 -9.1; 54 -9.1; 60 -9.1; 66 -9.1; 72 -9.0; 79 -8.8; 87 -8.8; 96 -8.7; 106 -8.7; 116 -8.5; 128 -8.2; 141 -7.8; 155 -7.9; 170 -7.7; 187 -7.1; 206 -6.6; 227 -6.0; 249 -5.4; 274 -4.8; 302 -4.1; 332 -3.3; 365 -2.5; 402 -1.8; 442 -1.3; 486 -0.8; 535 -0.1; 588 0.5; 647 0.8; 712 0.9; 783 0.5; 861 0.1; 947 -0.2; 1042 -0.3; 1146 -0.3; 1261 -0.4; 1387 -0.5; 1526 -0.2; 1678 0.4; 1846 0.8; 2031 0.8; 2234 0.5; 2457 -0.9; 2703 -2.8; 2973 -4.9; 3270 -4.7; 3597 -2.7; 3957 -0.7; 4353 1.0; 4788 2.2; 5267 1.9; 5793 1.0; 6373 -1.3; 7010 -5.8; 7711 -10.2; 8482 -7.8; 9330 -1.9; 10263 0.0; 11289 0.0; 12418 -2.5; 13660 -8.8; 15026 -13.6; 16529 -13.9; 18182 -11.8; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.3  | -9.2 dB  |
| Peaking | 171 Hz   | 0.94 | -4.1 dB  |
| Peaking | 3100 Hz  | 5.16 | -5.6 dB  |
| Peaking | 15205 Hz | 3.53 | -6.5 dB  |
| Peaking | 17637 Hz | 0.84 | -12.1 dB |
| Peaking | 649 Hz   | 2.64 | 1.8 dB   |
| Peaking | 5370 Hz  | 2.57 | 4.2 dB   |
| Peaking | 7868 Hz  | 3.05 | -12.1 dB |
| Peaking | 10744 Hz | 1.56 | 5.9 dB   |
| Peaking | 13885 Hz | 4.18 | -3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/SoundPeats%20Q8/SoundPeats%20Q8.png)