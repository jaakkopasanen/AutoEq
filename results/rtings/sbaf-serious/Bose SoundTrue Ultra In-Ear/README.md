# Bose SoundTrue Ultra In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 -0.2; 23 -0.3; 25 -0.4; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.6; 45 -0.6; 49 -0.6; 54 -0.6; 60 -0.6; 66 -0.7; 72 -0.6; 79 -0.5; 87 -0.5; 96 -0.6; 106 -0.7; 116 -0.7; 128 -0.7; 141 -0.7; 155 -0.9; 170 -1.2; 187 -1.2; 206 -1.1; 227 -0.8; 249 -0.4; 274 0.1; 302 0.6; 332 1.1; 365 1.5; 402 1.9; 442 2.2; 486 2.6; 535 3.0; 588 3.2; 647 3.5; 712 3.6; 783 3.0; 861 1.8; 947 0.5; 1042 -0.2; 1146 -0.5; 1261 -0.6; 1387 -1.0; 1526 -1.5; 1678 -1.8; 1846 -1.6; 2031 -1.4; 2234 -0.7; 2457 0.1; 2703 0.7; 2973 1.2; 3270 2.0; 3597 2.5; 3957 1.5; 4353 -0.3; 4788 -0.3; 5267 0.0; 5793 -0.4; 6373 -0.6; 7010 1.8; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundTrue Ultra In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundTrue Ultra In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 179 Hz  |  0.68 | -1.4 dB |
| Peaking | 641 Hz  |  0.83 | 6.0 dB  |
| Peaking | 1603 Hz |  0.35 | -3.7 dB |
| Peaking | 3258 Hz |  1.61 | 4.6 dB  |
| Peaking | 7082 Hz |  8.3  | 2.3 dB  |
| Peaking | 39 Hz   |  1.28 | -0.5 dB |
| Peaking | 760 Hz  |  6.64 | 0.7 dB  |
| Peaking | 984 Hz  |  6.5  | -0.7 dB |
| Peaking | 4483 Hz | 12.84 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20SoundTrue%20Ultra%20In-Ear/Bose%20SoundTrue%20Ultra%20In-Ear.png)