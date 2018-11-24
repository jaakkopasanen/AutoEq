# Bose SoundTrue Around-Ear II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.2; 25 0.3; 28 0.4; 31 0.6; 34 0.8; 37 1.1; 41 1.4; 45 1.7; 49 1.9; 54 2.2; 60 2.3; 66 2.3; 72 2.3; 79 2.1; 87 1.8; 96 1.5; 106 1.0; 116 0.6; 128 0.2; 141 -0.3; 155 -0.6; 170 -0.6; 187 -0.4; 206 -0.2; 227 -0.1; 249 0.6; 274 1.3; 302 1.8; 332 2.5; 365 3.1; 402 3.5; 442 3.7; 486 3.9; 535 4.0; 588 3.9; 647 3.5; 712 2.7; 783 1.8; 861 0.9; 947 0.2; 1042 0.0; 1146 0.3; 1261 0.4; 1387 0.3; 1526 0.0; 1678 -0.4; 1846 -0.6; 2031 -0.4; 2234 0.6; 2457 1.7; 2703 0.3; 2973 -0.5; 3270 -0.9; 3597 0.1; 3957 1.3; 4353 3.7; 4788 6.0; 5267 6.0; 5793 5.5; 6373 3.6; 7010 2.3; 7711 0.3; 8482 0.0; 9330 -0.4; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundTrue Around-Ear II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundTrue Around-Ear II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 64 Hz   |  1.08 | 3.1 dB  |
| Peaking | 367 Hz  |  2.26 | 2.3 dB  |
| Peaking | 565 Hz  |  1.35 | 4.5 dB  |
| Peaking | 813 Hz  |  0.06 | -0.9 dB |
| Peaking | 5266 Hz |  2.25 | 7.5 dB  |
| Peaking | 166 Hz  |  4    | -0.7 dB |
| Peaking | 2453 Hz |  6.25 | 2.4 dB  |
| Peaking | 3470 Hz |  3.11 | -2.0 dB |
| Peaking | 3682 Hz |  6.88 | 1.1 dB  |
| Peaking | 4569 Hz | 10.18 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bose%20SoundTrue%20Around-Ear%20II/Bose%20SoundTrue%20Around-Ear%20II.png)