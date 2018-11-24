# Bose SoundTrue Ultra In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 21 -0.6; 23 -0.6; 25 -0.6; 28 -0.6; 31 -0.6; 34 -0.5; 37 -0.5; 41 -0.4; 45 -0.3; 49 -0.3; 54 -0.3; 60 -0.3; 66 -0.5; 72 -0.6; 79 -0.7; 87 -0.8; 96 -1.0; 106 -1.1; 116 -1.2; 128 -1.2; 141 -1.2; 155 -1.5; 170 -1.9; 187 -1.8; 206 -1.6; 227 -1.3; 249 -0.9; 274 -0.6; 302 -0.2; 332 0.2; 365 0.5; 402 0.8; 442 1.1; 486 1.4; 535 1.8; 588 2.1; 647 2.5; 712 2.7; 783 2.5; 861 1.7; 947 0.5; 1042 -0.3; 1146 -0.7; 1261 -0.8; 1387 -1.0; 1526 -1.1; 1678 -1.4; 1846 -1.7; 2031 -1.8; 2234 -1.1; 2457 -0.3; 2703 -0.1; 2973 -0.3; 3270 -0.6; 3597 -0.7; 3957 -0.9; 4353 -1.6; 4788 -1.9; 5267 -3.0; 5793 -4.4; 6373 -4.4; 7010 -0.8; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -1.0; 11289 -0.2; 12418 0.0; 13660 0.0; 15026 -0.8; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundTrue Ultra In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundTrue Ultra In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.11 | -0.4 dB |
| Peaking | 180 Hz  | 1.12 | -1.7 dB |
| Peaking | 727 Hz  | 1.02 | 4.6 dB  |
| Peaking | 1176 Hz | 0.75 | -2.9 dB |
| Peaking | 5880 Hz | 3.78 | -4.9 dB |
| Peaking | 2018 Hz | 3.05 | -2.3 dB |
| Peaking | 2252 Hz | 1.19 | 2.4 dB  |
| Peaking | 3265 Hz | 0.46 | -1.0 dB |
| Peaking | 7618 Hz | 5.79 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundTrue%20Ultra%20In-Ear/Bose%20SoundTrue%20Ultra%20In-Ear.png)