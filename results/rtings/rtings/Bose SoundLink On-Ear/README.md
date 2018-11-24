# Bose SoundLink On-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -7.2; 23 -7.2; 25 -7.3; 28 -7.3; 31 -7.3; 34 -7.3; 37 -7.2; 41 -7.1; 45 -7.0; 49 -6.8; 54 -6.7; 60 -6.7; 66 -6.7; 72 -6.8; 79 -6.8; 87 -6.8; 96 -6.8; 106 -6.8; 116 -6.7; 128 -6.7; 141 -6.7; 155 -6.7; 170 -6.5; 187 -5.9; 206 -5.5; 227 -5.4; 249 -5.2; 274 -5.3; 302 -5.3; 332 -5.0; 365 -4.6; 402 -4.1; 442 -3.6; 486 -3.1; 535 -2.5; 588 -2.0; 647 -1.5; 712 -1.1; 783 -0.8; 861 -0.6; 947 -0.2; 1042 -0.1; 1146 -0.1; 1261 0.0; 1387 0.0; 1526 -0.1; 1678 -0.6; 1846 -1.1; 2031 -1.8; 2234 -1.8; 2457 -1.2; 2703 -1.9; 2973 -2.5; 3270 -2.4; 3597 -2.7; 3957 -3.4; 4353 -2.8; 4788 -1.0; 5267 1.9; 5793 2.6; 6373 0.2; 7010 -2.6; 7711 -3.8; 8482 -5.7; 9330 -7.8; 10263 -7.4; 11289 -3.4; 12418 -0.2; 13660 -0.3; 15026 -3.0; 16529 -7.5; 18182 -9.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundLink On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundLink On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.31 | -6.9 dB  |
| Peaking | 142 Hz   | 0.56 | -4.8 dB  |
| Peaking | 354 Hz   | 1.2  | -2.5 dB  |
| Peaking | 9445 Hz  | 3.02 | -8.3 dB  |
| Peaking | 18155 Hz | 1.6  | -10.3 dB |
| Peaking | 1166 Hz  | 1.6  | 0.9 dB   |
| Peaking | 4625 Hz  | 0.84 | -4.4 dB  |
| Peaking | 5592 Hz  | 3.04 | 7.6 dB   |
| Peaking | 13152 Hz | 2.96 | 3.1 dB   |
| Peaking | 16440 Hz | 4.68 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bose%20SoundLink%20On-Ear/Bose%20SoundLink%20On-Ear.png)