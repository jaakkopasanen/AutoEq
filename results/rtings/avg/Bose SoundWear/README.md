# Bose SoundWear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.3; 106 5.0; 116 5.1; 128 4.9; 141 3.8; 155 2.4; 170 1.1; 187 1.1; 206 2.0; 227 5.1; 249 3.2; 274 2.0; 302 0.5; 332 -0.6; 365 0.4; 402 -3.1; 442 -3.0; 486 -3.4; 535 -5.1; 588 -3.6; 647 -0.9; 712 -2.3; 783 -3.6; 861 -3.4; 947 -1.5; 1042 0.2; 1146 -0.5; 1261 -2.7; 1387 2.2; 1526 3.6; 1678 3.3; 1846 -0.3; 2031 -3.9; 2234 -4.7; 2457 -3.4; 2703 -3.9; 2973 -5.1; 3270 -8.0; 3597 -8.9; 3957 -7.2; 4353 -9.2; 4788 -8.4; 5267 -7.9; 5793 -2.3; 6373 -1.9; 7010 1.4; 7711 0.3; 8482 -2.2; 9330 -3.5; 10263 -1.6; 11289 -3.9; 12418 -9.6; 13660 -12.4; 15026 -12.2; 16529 -6.9; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundWear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundWear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.21 | 6.2 dB   |
| Peaking | 519 Hz   | 1.61 | -5.0 dB  |
| Peaking | 3460 Hz  | 2.2  | -7.6 dB  |
| Peaking | 4761 Hz  | 3.92 | -6.8 dB  |
| Peaking | 14253 Hz | 2    | -14.2 dB |
| Peaking | 179 Hz   | 4.22 | -2.7 dB  |
| Peaking | 232 Hz   | 6.29 | 3.5 dB   |
| Peaking | 1608 Hz  | 4.72 | 10.1 dB  |
| Peaking | 1760 Hz  | 1.65 | -4.2 dB  |
| Peaking | 7190 Hz  | 5.95 | 3.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundWear/Bose%20SoundWear.png)