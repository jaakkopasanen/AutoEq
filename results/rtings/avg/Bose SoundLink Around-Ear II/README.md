# Bose SoundLink Around-Ear II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 21 -4.1; 23 -4.1; 25 -4.1; 28 -4.1; 31 -4.0; 34 -3.8; 37 -3.6; 41 -3.3; 45 -3.0; 49 -2.8; 54 -2.6; 60 -2.4; 66 -2.4; 72 -2.4; 79 -2.6; 87 -2.6; 96 -2.8; 106 -2.9; 116 -3.1; 128 -3.2; 141 -3.2; 155 -3.2; 170 -3.1; 187 -2.9; 206 -2.8; 227 -2.9; 249 -2.6; 274 -2.5; 302 -2.5; 332 -2.4; 365 -2.3; 402 -2.4; 442 -2.4; 486 -2.2; 535 -2.1; 588 -1.9; 647 -1.9; 712 -1.7; 783 -1.2; 861 -0.5; 947 0.0; 1042 -0.2; 1146 -0.9; 1261 -1.7; 1387 -2.4; 1526 -2.6; 1678 -2.5; 1846 -5.0; 2031 -5.8; 2234 -4.6; 2457 -3.3; 2703 -3.4; 2973 -4.5; 3270 -5.2; 3597 -5.0; 3957 -4.4; 4353 -3.8; 4788 -1.4; 5267 2.8; 5793 -0.6; 6373 -1.5; 7010 0.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.7; 13660 -5.2; 15026 -6.4; 16529 -6.2; 18182 -5.1; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundLink Around-Ear II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundLink Around-Ear II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.82 | -3.9 dB |
| Peaking | 184 Hz   | 0.34 | -2.9 dB |
| Peaking | 2001 Hz  | 2.77 | -5.1 dB |
| Peaking | 3463 Hz  | 2.73 | -5.2 dB |
| Peaking | 16432 Hz | 1.37 | -7.3 dB |
| Peaking | 961 Hz   | 6.8  | 1.3 dB  |
| Peaking | 4405 Hz  | 6.08 | -2.1 dB |
| Peaking | 5269 Hz  | 9.75 | 4.5 dB  |
| Peaking | 12516 Hz | 1.53 | 2.9 dB  |
| Peaking | 13771 Hz | 3.36 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundLink%20Around-Ear%20II/Bose%20SoundLink%20Around-Ear%20II.png)