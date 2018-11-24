# Bose SoundTrue Around-Ear II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.5; 25 0.5; 28 0.6; 31 0.7; 34 0.8; 37 1.0; 41 1.2; 45 1.4; 49 1.6; 54 1.8; 60 2.0; 66 2.2; 72 2.3; 79 2.3; 87 2.2; 96 1.9; 106 1.5; 116 1.1; 128 0.7; 141 0.3; 155 0.1; 170 0.0; 187 0.2; 206 0.3; 227 0.4; 249 1.1; 274 1.9; 302 2.7; 332 3.5; 365 4.1; 402 4.6; 442 4.8; 486 5.1; 535 5.2; 588 5.0; 647 4.5; 712 3.5; 783 2.3; 861 1.1; 947 0.2; 1042 0.1; 1146 0.5; 1261 0.6; 1387 0.3; 1526 -0.3; 1678 -0.7; 1846 -0.6; 2031 -0.0; 2234 1.1; 2457 2.2; 2703 0.9; 2973 0.6; 3270 1.0; 3597 2.3; 3957 2.5; 4353 3.7; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundTrue Around-Ear II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundTrue Around-Ear II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 68 Hz   | 1.33 | 2.4 dB  |
| Peaking | 519 Hz  | 1.11 | 5.8 dB  |
| Peaking | 991 Hz  | 1.59 | -1.5 dB |
| Peaking | 4928 Hz | 2.54 | 5.5 dB  |
| Peaking | 6167 Hz | 4.86 | 3.9 dB  |
| Peaking | 196 Hz  | 2.09 | -1.0 dB |
| Peaking | 336 Hz  | 3.79 | 0.9 dB  |
| Peaking | 1760 Hz | 4.86 | -1.3 dB |
| Peaking | 2413 Hz | 7.55 | 1.9 dB  |
| Peaking | 8233 Hz | 4.19 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20SoundTrue%20Around-Ear%20II/Bose%20SoundTrue%20Around-Ear%20II.png)