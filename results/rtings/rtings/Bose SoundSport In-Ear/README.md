# Bose SoundSport In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 4.3; 72 3.1; 79 2.1; 87 1.1; 96 0.3; 106 -0.4; 116 -0.9; 128 -1.3; 141 -1.6; 155 -1.8; 170 -2.0; 187 -2.1; 206 -2.1; 227 -2.1; 249 -2.1; 274 -2.2; 302 -2.3; 332 -2.3; 365 -2.5; 402 -2.7; 442 -2.7; 486 -2.7; 535 -2.6; 588 -2.3; 647 -1.7; 712 -1.0; 783 -0.3; 861 0.1; 947 0.2; 1042 -0.1; 1146 -0.6; 1261 -1.2; 1387 -2.0; 1526 -2.7; 1678 -3.2; 1846 -3.4; 2031 -3.1; 2234 -1.9; 2457 -0.0; 2703 0.9; 2973 1.6; 3270 1.7; 3597 1.6; 3957 1.2; 4353 0.1; 4788 -0.2; 5267 0.6; 5793 1.3; 6373 -1.7; 7010 -4.2; 7711 -2.0; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.53 | 8.4 dB  |
| Peaking | 209 Hz  | 0.22 | -3.8 dB |
| Peaking | 1795 Hz | 1.44 | -8.3 dB |
| Peaking | 1800 Hz | 0.55 | 5.4 dB  |
| Peaking | 7052 Hz | 5.54 | -5.2 dB |
| Peaking | 57 Hz   | 1.21 | -1.8 dB |
| Peaking | 59 Hz   | 2.49 | 3.1 dB  |
| Peaking | 553 Hz  | 3.74 | -0.8 dB |
| Peaking | 848 Hz  | 4.61 | 0.8 dB  |
| Peaking | 3003 Hz | 5.63 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bose%20SoundSport%20In-Ear/Bose%20SoundSport%20In-Ear.png)