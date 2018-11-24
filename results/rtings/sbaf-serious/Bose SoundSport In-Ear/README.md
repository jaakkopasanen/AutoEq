# Bose SoundSport In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.3; 66 4.1; 72 3.1; 79 2.3; 87 1.5; 96 0.8; 106 0.1; 116 -0.3; 128 -0.7; 141 -1.0; 155 -1.2; 170 -1.4; 187 -1.5; 206 -1.6; 227 -1.7; 249 -1.6; 274 -1.6; 302 -1.5; 332 -1.4; 365 -1.5; 402 -1.7; 442 -1.6; 486 -1.4; 535 -1.4; 588 -1.2; 647 -0.7; 712 -0.1; 783 0.2; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -1.0; 1387 -2.0; 1526 -3.1; 1678 -3.6; 1846 -3.4; 2031 -2.7; 2234 -1.4; 2457 0.4; 2703 1.5; 2973 2.7; 3270 3.6; 3597 3.8; 3957 2.4; 4353 0.1; 4788 -0.3; 5267 1.0; 5793 2.7; 6373 0.8; 7010 -1.7; 7711 -0.9; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.4  | 9.7 dB  |
| Peaking | 109 Hz  | 0.41 | -5.8 dB |
| Peaking | 1780 Hz | 2.47 | -4.1 dB |
| Peaking | 2977 Hz | 3.04 | 2.4 dB  |
| Peaking | 3558 Hz | 4.41 | 3.3 dB  |
| Peaking | 37 Hz   | 3.21 | -0.5 dB |
| Peaking | 888 Hz  | 4.06 | 1.0 dB  |
| Peaking | 4636 Hz | 6.22 | -1.5 dB |
| Peaking | 5796 Hz | 4.89 | 3.0 dB  |
| Peaking | 7107 Hz | 6.41 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20SoundSport%20In-Ear/Bose%20SoundSport%20In-Ear.png)