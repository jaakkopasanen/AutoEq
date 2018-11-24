# Bose SoundLink Around-Ear II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 21 -4.1; 23 -4.1; 25 -4.1; 28 -4.1; 31 -4.0; 34 -3.8; 37 -3.6; 41 -3.3; 45 -3.0; 49 -2.8; 54 -2.6; 60 -2.4; 66 -2.4; 72 -2.4; 79 -2.6; 87 -2.6; 96 -2.8; 106 -2.9; 116 -3.1; 128 -3.2; 141 -3.2; 155 -3.2; 170 -3.1; 187 -2.9; 206 -2.8; 227 -2.9; 249 -2.6; 274 -2.5; 302 -2.5; 332 -2.4; 365 -2.3; 402 -2.4; 442 -2.4; 486 -2.2; 535 -2.1; 588 -1.9; 647 -1.9; 712 -1.7; 783 -1.2; 861 -0.5; 947 0.0; 1042 -0.2; 1146 -0.9; 1261 -1.7; 1387 -2.4; 1526 -2.6; 1678 -2.5; 1846 -5.0; 2031 -5.8; 2234 -4.6; 2457 -3.3; 2703 -3.1; 2973 -4.0; 3270 -4.5; 3597 -4.0; 3957 -3.2; 4353 -2.5; 4788 0.4; 5267 5.4; 5793 1.9; 6373 -0.2; 7010 1.1; 7711 0.3; 8482 0.0; 9330 -1.7; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 -1.9; 15026 -3.8; 16529 -3.2; 18182 -0.8; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundLink Around-Ear II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundLink Around-Ear II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 32 Hz    |  0.05 | -3.1 dB |
| Peaking | 1990 Hz  |  3.16 | -4.9 dB |
| Peaking | 3502 Hz  |  1.69 | -4.2 dB |
| Peaking | 5314 Hz  |  6.42 | 7.3 dB  |
| Peaking | 15628 Hz |  2.35 | -4.3 dB |
| Peaking | 37 Hz    |  0.39 | -1.7 dB |
| Peaking | 61 Hz    |  0.92 | 2.2 dB  |
| Peaking | 951 Hz   |  2.65 | 3.3 dB  |
| Peaking | 991 Hz   |  1.35 | -1.9 dB |
| Peaking | 7196 Hz  | 11    | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bose%20SoundLink%20Around-Ear%20II/Bose%20SoundLink%20Around-Ear%20II.png)